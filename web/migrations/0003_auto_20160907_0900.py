# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-07 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20160907_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverimage',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='cover/'),
        ),
    ]
