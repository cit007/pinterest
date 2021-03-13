from django.forms import ModelForm
from django import forms

from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    desc = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable'}))

    class Meta:
        model = Project
        fields = ['title', 'image', 'desc']
