# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-03-18 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20180318_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date released'),
        ),
    ]