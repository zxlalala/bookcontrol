# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20170410_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
