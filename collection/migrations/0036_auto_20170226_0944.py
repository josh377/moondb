# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0035_userdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='first_name',
            field=models.CharField(default=123, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='last_name',
            field=models.CharField(default=123, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='ape_index',
            field=models.CharField(max_length=255, verbose_name='Ape Index'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='moonboardlocation',
            field=models.CharField(max_length=255, verbose_name='Moonboard Location'),
        ),
    ]
