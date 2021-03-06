# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_lens_online', '0002_auto_20160505_1832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='item_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='user_id',
            new_name='rater',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='action',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='id',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='id',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='rater',
            name='sex',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='rater',
            name='occupation',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='rater',
            name='user_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
