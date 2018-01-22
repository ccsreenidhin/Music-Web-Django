# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

def get_upload_path(instance, filename):
    return 'users/{0}/{1}'.format(instance.user.username, filename)

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class MusicCollection(models.Model):
    user = models.ForeignKey(User, null=True)
    document = models.FileField(upload_to=get_upload_path)



