# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-29 23:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_auto_20180129_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='title',
        ),
        migrations.AddField(
            model_name='upload',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='upload',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='upload',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='upload',
            name='myfile',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]