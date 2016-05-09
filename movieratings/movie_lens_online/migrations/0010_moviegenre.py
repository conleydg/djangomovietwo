# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_lens_online', '0009_rating_submit_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moviegenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unknown', models.IntegerField(default=0)),
                ('Action', models.IntegerField(default=0)),
                ('Adventure', models.IntegerField(default=0)),
                ('Animation', models.IntegerField(default=0)),
                ('Childrens', models.IntegerField(default=0)),
                ('Comedy', models.IntegerField(default=0)),
                ('Crime', models.IntegerField(default=0)),
                ('Documentary', models.IntegerField(default=0)),
                ('Drama', models.IntegerField(default=0)),
                ('Fantasy', models.IntegerField(default=0)),
                ('FilmNoir', models.IntegerField(default=0)),
                ('Horror', models.IntegerField(default=0)),
                ('Musical', models.IntegerField(default=0)),
                ('Mystery', models.IntegerField(default=0)),
                ('Romance', models.IntegerField(default=0)),
                ('SciFi', models.IntegerField(default=0)),
                ('Thriller', models.IntegerField(default=0)),
                ('War', models.IntegerField(default=0)),
                ('Western', models.IntegerField(default=0)),
                ('movie', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_lens_online.Movie')),
            ],
        ),
    ]