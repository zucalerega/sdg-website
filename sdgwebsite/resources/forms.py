from django import forms

from .models import Article, Source

class ArticleForm(forms.ModelForm):
    author = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Author..."}))

    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Title..."}))
    topic = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Topic..."}))

    content = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Write article here..."}))
    visuals = forms.FileField(required=False)
    sources = forms.URLField()
    
    class Meta:
        model=Article
        fields=['author', 'topic', 'title', 'content', 'visuals', 'sources']
