from django.urls import include, re_path

from . import views
app_name = 'misc'

api_urlpatterns = [
]

page_urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]

urlpatterns = [
    re_path(r'', include((page_urlpatterns, 'page'), namespace='page')),
    re_path(r'', include((api_urlpatterns, 'api'), namespace='api')),
]
