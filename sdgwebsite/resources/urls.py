from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('article/new/', views.publish_article, name="publish_article"),

    path('article/<str:unique_id>/', views.article_view, name='article_view'),
    path('home/', views.homepage_view, name='homepage_view'),
    path('article/', views.article_home_view, name="article_home_view"),
]
