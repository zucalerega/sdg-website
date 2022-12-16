from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('article/', views.article_view, name='article_view'),
    path('home/', views.homepage_view, name='homepage_view'),

]
