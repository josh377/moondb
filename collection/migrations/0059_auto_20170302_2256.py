# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0058_auto_20170301_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climb',
            name='global_repeats',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
