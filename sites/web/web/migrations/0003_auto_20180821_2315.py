# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-21 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20180729_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]