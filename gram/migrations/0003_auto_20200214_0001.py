# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-13 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0002_auto_20200213_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='prof_picture',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='kent.jpg', upload_to='pictures/'),
        ),
    ]
