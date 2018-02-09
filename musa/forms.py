from django import forms
from django.contrib.auth.models import User
from musa.models import UserProfile, MusicCollection



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('fullname', 'favourite_music', 'about', 'picture',)


class MusicForm(forms.ModelForm):
    class Meta:
	model = MusicCollection
	fields = ('document',)

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    content = forms.CharField(required=True,
        widget=forms.Textarea)
