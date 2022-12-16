from django.shortcuts import render, redirect, HttpResponse
from resources.models import Article, Source

# Create your views here.
def homepage_view(request):
    context = {}
    return render(request, "homepage.html", context)

    
def article_view(request):
    context = {}
    return render(request, "article.html", context)
