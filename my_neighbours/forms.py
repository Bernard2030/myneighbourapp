from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        exclude = ['username','neighbourhood','profile_pic'] 

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['owner','neighbourhood']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['username','post']                      