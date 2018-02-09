# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone

from django.core.validators import RegexValidator

# Create your models here.


def get_upload_path(instance, filename):
    return 'users/{0}/{1}'.format(instance.user.username, filename)



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fullname = models.CharField(max_length = 70, blank=True)
    favourite_music = models.CharField(max_length = 70,blank=True)
    about = models.TextField(max_length=300, blank=True)
    picture = models.ImageField(upload_to='profile_images', default='/profile_images/avatar.jpeg')

    def __str__(self):
        return self.user.username


class MusicCollection(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=70, blank=True, null =True)
    document = models.FileField(upload_to=get_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.user.username
