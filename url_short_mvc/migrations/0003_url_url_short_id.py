# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-18 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_short_mvc', '0002_url_short_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='url_short_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
