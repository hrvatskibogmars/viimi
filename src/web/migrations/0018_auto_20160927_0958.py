# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20160927_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='text',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
