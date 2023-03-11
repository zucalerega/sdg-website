from django.shortcuts import render, redirect, HttpResponse
from resources.models import Article, Source
from .forms import ArticleForm
from django.contrib import messages
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

def article_home_view(request):
    articles = Article.objects.all().order_by('-date_published')

    context = {"articles": articles}
    return render(request, "articlehome.html", context)

def publish_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        # form.save()
        article = Article.objects.create(title=form.cleaned_data.get('title'), 
                                         author=form.cleaned_data.get('author'),
                                         content=form.cleaned_data.get('content'),
                                         visuals=form.cleaned_data.get('visuals'),
                                         topic=form.cleaned_data.get('topic')
                                         )
        article.save()
        return redirect('resources:homepage_view')

    messages.success(request, f'Article published!')
    context = {'form': form}
    return render(request, "publish.html", context)
    # return redirect('resources:hompage_view')

