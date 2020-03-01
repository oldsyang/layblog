from django.urls import include, re_path

from . import api_views, page_views

app_name = 'article'

v0_api_urlpatterns = [
    re_path(r'articles/$', api_views.ArticleListAPIView.as_view(), name='article.list'),
    re_path(r'articles/(?P<acode>[^/]+)/$', api_views.ArticleDetailAPIView.as_view(), name='article.detail'),
]

page_urlpatterns = [
    re_path(r'^article.html/?$', page_views.article_list, name='article.list'),
    re_path(r'^articles/(?P<acode>[^/]+)/$', page_views.article_details, name='article.detail'),
]

urlpatterns = [
    re_path(r'', include((page_urlpatterns, 'page'), namespace='page')),
    re_path(r'api/v0/', include((v0_api_urlpatterns, 'api.v0'), namespace='api.vo')),
]


