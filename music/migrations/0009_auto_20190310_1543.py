# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2019-03-10 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_album_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
