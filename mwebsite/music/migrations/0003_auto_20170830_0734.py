# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(upload_to=b''),
        ),
    ]
