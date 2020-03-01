import arrow
import markdown2
from django.conf import settings
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from rest_framework import serializers

from .models import Article, ArticleDetail


class ArticleDetailSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
        mark_safe(markdown2.markdown(force_text(obj.content),
                                     extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables", "spoiler",
                                             "toc"]))

    class Meta:
        model = ArticleDetail
        fields = (
            'content',
        )


class ArticleListSerializer(serializers.ModelSerializer):
    publish_date = serializers.SerializerMethodField()

    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.category.title

    def get_publish_date(self, obj):
        return arrow.get(obj.created).to(settings.TIME_ZONE).format('YYYY-MM-DD')

    class Meta:
        model = Article
        fields = (
            'id', 'title', 'cover', 'publish_date', 'category', 'summary', 'acode'
        )
