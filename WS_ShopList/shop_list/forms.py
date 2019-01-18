from django import forms
from django.contrib.auth.models import User


class PostForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
