from django.shortcuts import render, redirect, HttpResponse
from resources.models import Article, Source

# Create your views here.
def homepage_view(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "homepage.html", context)

    
def article_view(request, unique_id):
    article = Article.objects.filter(unique_id=unique_id)[0]
    sources = article.sources.all()
    context = {"article": article, "sources": sources}
    return render(request, "article.html", context)
