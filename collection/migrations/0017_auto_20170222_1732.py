# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0016_auto_20170222_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climb',
            name='grade',
            field=models.CharField(choices=[('test', '8b'), ('8a+', '8a+'), ('8a', '8a'), ('7c+', '7c+'), ('7c', '7c'), ('7b+', '7b+'), ('7b', '7b'), ('7a+', '7a+'), ('7a', '7a'), ('6c+', '6c+'), ('6c', '6c'), ('6b+', '6b+')], max_length=255),
        ),
    ]