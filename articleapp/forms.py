from django.forms import ModelForm
from django import forms

from articleapp.models import Article

from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'editable'}))

    class Meta:
        model = Article
        fields = ['title', 'image', 'content', 'project']
