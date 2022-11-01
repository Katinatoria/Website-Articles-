from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

def index(request):
    title = str(Article.article_title)
    return render(request, 'main/index.html', {'title_ar': title})

def arcan(request):
   allArticles = Article.objects.all()
   return render(request, 'main/arcan.html', {'allArticles': allArticles})

