from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from genfier.models import Document, UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
