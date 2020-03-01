from django.shortcuts import redirect, render

# Create your views here.
from articles.models import Article


def index(request):
    return redirect('article.html')
