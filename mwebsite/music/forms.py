from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )




class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['text','image','body']
        labels = {'text': 'Blog name','image':'','body':''}
        widgets = {'body': forms.Textarea(attrs={'cols': 80})}


class BlogEdit(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['image','body']
        labels = {'text': 'Blog name','image':'','body':''}
        widgets = {'body': forms.Textarea(attrs={'cols': 80})}



