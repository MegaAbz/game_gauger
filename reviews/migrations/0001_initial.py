# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-28 15:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(choices=[(b'', b'Please Select'), (b'ACTION', b'Action'), (b'ACTIONADVENTURE', b'Action-Adventure'), (b'ADVENTURE', b'Adventure'), (b'MISC', b'Misc'), (b'RPG', b'Role-Playing Game'), (b'SIMULATION', b'Simulation'), (b'STRATEGY', b'Strategy'), (b'SPORTS', b'Sports'), (b'PUZZLE', b'Puzzle')], default=b'Please Select', max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=100, unique=True)),
                ('genre', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=50)),
                ('developer', models.CharField(max_length=50)),
                ('logo', models.ImageField(default=b'None/no-img.jpg', upload_to=b'media/')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now=True)),
                ('user_name', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=2000)),
                ('rating', models.IntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Game')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to=b'profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
