# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-07 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverimage',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
