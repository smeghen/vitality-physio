from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    """
    Form for Blog model that uses all fields
    """
    class Meta:
        model = Blog
        fields = ['author', 'subject', 'content']
