# -*- coding:utf8 -*-
import logging

from django.db import models
from django.db.models import F
from django.utils import timezone
from model_utils import Choices
from model_utils.models import TimeStampedModel

from common import constants, tools
from common.exceptions import ErrorCode
from common.rest import Error

logger = logging.getLogger(__name__)


class Category(models.Model):
    """分类表"""
    title = models.CharField(verbose_name="分类名称", max_length=63, unique=True)

    class Meta:
        verbose_name_plural = verbose_name = '文章分类'

    @classmethod
    def category_list(cls):
        return {item.id: item.title for item in cls.objects.all()}

    def __repr__(self):
        return '<%s %d: %s>' % (self.__class__.__name__, self.id, self.title)

    def __str__(self):
        return self.title


class Article(TimeStampedModel):
    """文章表"""

    Format = Choices(
        (constants.ArticleFormat.html.value, '富文本'),
        (constants.ArticleFormat.markdown.value, 'markdown'),
        (constants.ArticleFormat.text.value, '字符串')
    )

    Status = Choices(
        (constants.ArticleStatus.default.value, '草稿'),
        (constants.ArticleStatus.publish.value, '已发布'),
    )

    acode = models.CharField(verbose_name='对外标识', unique=True, max_length=64, default=tools.generate_acode)
    title = models.CharField(verbose_name="文章标题", max_length=127)
    cover = models.FileField(verbose_name="封面", max_length=127, blank=True, default='')
    summary = models.CharField(verbose_name="文章简介", max_length=255, default='')
    category = models.ForeignKey(verbose_name="文章类型", to="Category", on_delete=models.SET_NULL, null=True)
    password = models.CharField(verbose_name="自定义密码", max_length=31, default='', blank=True)
    format = models.PositiveSmallIntegerField(verbose_name='文档格式', default=constants.ArticleFormat.markdown.value,
                                              choices=Format)

    publish_date = models.DateTimeField(verbose_name='发布时间', default=timezone.now)
    status = models.PositiveSmallIntegerField(verbose_name='文档状态', default=constants.ArticleStatus.default.value,
                                              choices=Status)

    class Meta:
        verbose_name_plural = verbose_name = '文章表'

    @classmethod
    def get(cls, *args, **kwargs):
        try:
            obj = cls.objects.get(*args, **kwargs)
        except cls.DoesNotExist:
            logger.warning('未找到文章')
            return
        return obj

    @classmethod
    def article_list_count(cls):
        return cls.objects.count()

    def __repr__(self):
        return '<%s %d: %s>' % (self.__class__.__name__, self.id, self.title)

    def __str__(self):
        return self.title


class ArticleDetail(TimeStampedModel):
    """文章内容表"""
    content = models.TextField(verbose_name="文章内容")
    article = models.OneToOneField(verbose_name="所属文章", to="Article", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = verbose_name = '文章内容'

    @classmethod
    def get_content_by_article(cls, *args, **kwargs):
        try:
            obj = cls.objects.get(*args, **kwargs)
        except cls.DoesNotExist:
            raise Error(ErrorCode.NOT_FOUND, message='未找到文章')
        return obj

    def __repr__(self):
        return '<%s %d: %s content>' % (self.__class__.__name__, self.article.id, self.article.title)

    def __str__(self):
        return self.article.title


class Tag(models.Model):
    """标签表"""
    title = models.CharField(verbose_name="标签名", max_length=63, unique=True)

    class Meta:
        verbose_name_plural = verbose_name = '标签'

    def __repr__(self):
        return '<%s %d: %s>' % (self.__class__.__name__, self.id, self.title)

    def __str__(self):
        return self.title


class Article2Tag(models.Model):
    """文章内容表"""
    tag = models.ForeignKey(verbose_name="所属标签", to="Tag", on_delete=models.CASCADE)
    article = models.ForeignKey(verbose_name="文章", to="Article", on_delete=models.CASCADE)

    @classmethod
    def article_tag_list(cls):
        query_data = cls.objects.annotate(title=F('tag__title')).filter(article__isnull=False).select_related(
            'tag').only('tag_id', 'tag__title').values('tag_id', 'title').distinct()

        return {item['tag_id']: item['title'] for item in query_data}

    class Meta:
        verbose_name_plural = verbose_name = '文章标签关系'
        unique_together = [
            ("tag", "article")
        ]

    def __repr__(self):
        return '<%s [tag %d: %s, article %d: %s]>' % (
            self.__class__.__name__, self.tag.id, self.tag.title, self.article.id, self.article.title)

    def __str__(self):
        return self.tag.title + ":" + self.article.title
