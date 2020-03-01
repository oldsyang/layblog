# Generated by Django 2.2.10 on 2020-03-01 13:25

import common.tools
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('acode', models.CharField(default=common.tools.generate_acode, max_length=64, unique=True, verbose_name='对外标识')),
                ('title', models.CharField(max_length=127, verbose_name='文章标题')),
                ('cover', models.FileField(blank=True, default='', max_length=127, upload_to='', verbose_name='封面')),
                ('summary', models.CharField(default='', max_length=255, verbose_name='文章简介')),
                ('password', models.CharField(blank=True, default='', max_length=31, verbose_name='自定义密码')),
                ('format', models.PositiveSmallIntegerField(choices=[(1, '富文本'), (2, 'markdown'), (3, '字符串')], default=2, verbose_name='文档格式')),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '草稿'), (2, '已发布')], default=1, verbose_name='文档状态')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63, unique=True, verbose_name='分类名称')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63, unique=True, verbose_name='标签名')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', verbose_name='所属文章')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='articles.Category', verbose_name='文章类型'),
        ),
        migrations.CreateModel(
            name='Article2Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', verbose_name='文章')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Tag', verbose_name='所属标签')),
            ],
            options={
                'unique_together': {('tag', 'article')},
            },
        ),
    ]
