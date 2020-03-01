from django.conf import settings
from django.shortcuts import render

from .models import Article, Article2Tag, ArticleDetail, Category


def article_list(request):
    if request.method == "GET":
        count = Article.article_list_count()
        tag_list = Article2Tag.article_tag_list()
        category_list = Category.category_list()
        json_data = {
            'article_count': count,
            'work_count': 50,
            'page_views': 5000,
            "tag_list": tag_list,
            'category_list': category_list
        }
        json_data.update(settings.SITE_INFO)

        return render(request, 'article/index.html', json_data)


def article_details(request, acode):
    if request.method == "GET":
        count = Article.article_list_count()
        tag_list = Article2Tag.article_tag_list()
        article = Article.get(acode=acode)

        json_data = {
            'article_count': count,
            'work_count': 50,
            'page_views': 5000,
            'tag_list': tag_list,
            "article": article,
            'content': ArticleDetail.get_content_by_article(article__acode=acode).content
        }
        json_data.update(settings.SITE_INFO)

        return render(request, 'article/detail.html', json_data)


def page_not_found(request, *args, **kwargs):
    return render(request, "404.html")
