# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(default=all, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='permission',
            field=models.IntegerField(default=1),
        ),
    ]
