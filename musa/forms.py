from django import forms
from django.contrib.auth.models import User
from musa.models import UserProfile, MusicCollection



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('fullname', 'phone', 'address', 'favourite_music', 'about', 'picture',)


class MusicForm(forms.ModelForm):
    class Meta:
	model = MusicCollection
	fields = ('document',)


