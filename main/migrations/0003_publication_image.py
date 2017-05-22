# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-22 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='image',
            field=models.ImageField(default=1, upload_to='public/images', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
