# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 09:10
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_ourservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keith_text', tinymce.models.HTMLField(blank=True, max_length=10000)),
                ('keith_cv', models.FileField(blank=True, null=True, upload_to='cv/')),
                ('izabela_text', tinymce.models.HTMLField(blank=True, max_length=10000)),
                ('izabela_cv', models.FileField(blank=True, null=True, upload_to='cv/')),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['order'], 'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='coverimage',
            options={'verbose_name': 'Home Cover Image', 'verbose_name_plural': 'Home Cover Images'},
        ),
        migrations.AlterModelOptions(
            name='ourservices',
            options={'verbose_name': 'Our Service', 'verbose_name_plural': 'Our Services'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['order'], 'verbose_name': 'Sample Project', 'verbose_name_plural': 'Sample Projects'},
        ),
        migrations.AlterField(
            model_name='ourservices',
            name='text',
            field=tinymce.models.HTMLField(blank=True, max_length=10000),
        ),
    ]
