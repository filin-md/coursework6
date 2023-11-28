from django.shortcuts import render

from blog.models import Article


# Create your views here.

def random_articles():
    article = Article.objects.all()

    return article