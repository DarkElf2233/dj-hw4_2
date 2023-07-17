
from django.shortcuts import render
from .models import Article


def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/news.html', {'articles': articles})
