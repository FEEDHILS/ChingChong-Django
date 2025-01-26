from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class PostsCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['rating', 'review']