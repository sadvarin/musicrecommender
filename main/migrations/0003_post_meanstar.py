# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-09 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_videourl'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='meanstar',
            field=models.FloatField(default=0.0),
        ),
    ]
