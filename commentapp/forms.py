from django.forms import ModelForm
from django import forms

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    # content = forms.CharField(
    #     widget=forms.Textarea(attrs={'class': 'editable'}))

    class Meta:
        model = Comment
        fields = ['content']
