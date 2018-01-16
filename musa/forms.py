from django import forms
from django.contrib.auth.models import User
from musa.models import UserProfile, MusicCollection


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


class MusicForm(forms.ModelForm):
    class Meta:
	model = MusicCollection
	fields = ('document', )
