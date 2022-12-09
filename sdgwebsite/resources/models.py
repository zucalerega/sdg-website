from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Source(models.Model):
    link = models.CharField(max_length=1_000, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

    # TODO could name the link with a function instead of user prompt


class Article(models.Model):
    # blank and null prevent database errors
    title = models.CharField(max_length=250, blank=True, null=True)
    # user saved as author, idk if we should cascade, that will delete the article if the account is
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # source can have multiple Articles and Article can have multiple Sources
    sources = models.ManyToManyField(Source)
    # automatically records the most recent update
    date_published = models.DateField(auto_now=True)
    # want to have set categories to choose from for sorting purposes
    topic = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    # TODO could add functions for sorting


# TODO could add class for visualizations
    
