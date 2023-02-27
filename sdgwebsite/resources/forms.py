from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    content = forms.TextField(widget=forms.TextInput(attrs={"placeholder":"Write article here..."}))
    visuals = forms.FileField()