# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0004_auto_20160227_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedshift',
            name='cover_requested',
            field=models.BooleanField(default=False),
        ),
    ]
