# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0004_auto_20170123_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_cover',
            field=models.FilePathField(path='/Users/CCallahanIV/Documents/CodeFellows/401/assignments/week6/django-imager/imagersite/MEDIA/photos'),
        ),
    ]
