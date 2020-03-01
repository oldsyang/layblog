# -*- coding: utf-8 -*-
from django_validator.decorators import GET
from rest_framework import generics

from common.pagination import ViewPagination
from .models import Article, ArticleDetail
from .serializers import ArticleDetailSerializer, ArticleListSerializer


class ArticleListAPIView(generics.ListAPIView):
    pagination_class = ViewPagination
    queryset = Article.objects.all().order_by('-publish_date')
    serializer_class = ArticleListSerializer

    @GET('category', type='int', default=0)
    @GET('tag', type='int', default=0)
    def filter_queryset(self, queryset, category, tag):
        if category:
            queryset = queryset.filter(category_id=category).select_related('category')
        if tag:
            queryset = queryset.filter(article2tag__tag_id=tag)

        return queryset


class ArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = ArticleDetail.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_url_kwarg = 'acode'
    lookup_field = 'article__acode'
