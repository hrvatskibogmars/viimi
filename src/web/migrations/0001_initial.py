# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-07 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoverImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.FileField(blank=True, null=True, upload_to='zastupstva/')),
                ('order', models.CharField(blank=True, max_length=15)),
                ('text', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.FileField(blank=True, null=True, upload_to=b'')),
                ('order', models.CharField(blank=True, max_length=15)),
                ('text', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
