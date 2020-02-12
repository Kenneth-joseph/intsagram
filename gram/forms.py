from .models import Post
from django import forms


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile', 'pub_date']
