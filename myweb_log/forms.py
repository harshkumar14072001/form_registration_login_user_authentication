from django import forms
from django.contrib.auth.models import User
from .models import *
class registration(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','email','password']

class postform(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'