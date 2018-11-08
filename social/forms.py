from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.posts
        fields = ['title', 'body']

class CreateBlogpost(forms.ModelForm):
    class Meta:
        model = models.blogpost
        fields = ['title', 'body']
