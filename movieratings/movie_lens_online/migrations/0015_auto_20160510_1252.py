# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_lens_online', '0014_auto_20160510_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]