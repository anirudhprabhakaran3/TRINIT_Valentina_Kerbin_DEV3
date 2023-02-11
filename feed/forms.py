from django import forms
from feed.models import Comment, Post


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']