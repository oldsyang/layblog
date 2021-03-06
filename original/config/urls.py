"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path('', include('articles.urls', namespace='article')),
    re_path('', include('misc.urls', namespace='misc')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'admin/', admin.site.urls),
        re_path(r'mdeditor/', include('mdeditor.urls')),
        re_path(r'^media/(?P<path>.*)$', static.serve, {"document_root": settings.MEDIA_ROOT}, name='media'),
    ]

handler404 = 'articles.page_views.page_not_found'
