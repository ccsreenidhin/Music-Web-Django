# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musa', '0006_auto_20170920_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
