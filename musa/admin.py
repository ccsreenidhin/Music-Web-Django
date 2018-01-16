# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from musa.models import UserProfile, MusicCollection

admin.site.register(UserProfile)


admin.site.register(MusicCollection)

# Register your models here.
