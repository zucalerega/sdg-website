from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('article/<str:unique_id>/', views.article_view, name='article_view'),
    path('home/', views.homepage_view, name='homepage_view'),
    path('articles/', views.article_home_view, name="article_home_view"),
]
