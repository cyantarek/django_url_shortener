# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-18 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_short_mvc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='short_url',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
