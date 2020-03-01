# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Article, Article2Tag, ArticleDetail, Category, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'password', 'cover', 'category', 'summary', 'format', 'publish_date')
    search_fields = ('title', 'category',)
    ordering = ('-created',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    ordering = ('-id',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('id', 'title')
    ordering = ('id',)


@admin.register(ArticleDetail)
class ArticleDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'article')
    search_fields = ('id', 'article__title')
    ordering = ('-created',)


@admin.register(Article2Tag)
class Article2TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'tag')
    search_fields = ('id', 'article__title', 'tag__title')
    ordering = ('id',)
