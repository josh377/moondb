# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0017_auto_20170222_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climb',
            name='grade',
            field=models.CharField(choices=[('13', '8b'), ('12', '8a+'), ('11', '8a'), ('10', '7c+'), ('9', '7c'), ('8', '7b+'), ('8', '7b'), ('7', '7a+'), ('6', '7a'), ('5', '6c+'), ('4', '6c'), ('3', '6b+')], max_length=255),
        ),
    ]
