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
class CreateBlog(forms.ModelForm):
    class Meta:
        model = models.blog
        fields = ['blogname', 'about']

class CreateBlogtags(forms.ModelForm):
    class Meta:
        model = models.blogtags
        fields = ['tags']

class CreateComment(forms.ModelForm):
    class Meta:
        model = models.comments
        fields = ['content']
