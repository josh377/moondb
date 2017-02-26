# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0028_auto_20170224_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climb',
            name='stars',
            field=models.IntegerField(blank=True, choices=[(3, '3'), (2, '2'), (1, '1'), (0, '0')]),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='stars',
            field=models.IntegerField(choices=[(3, '3'), (2, '2'), (1, '1'), (0, '0')]),
        ),
    ]
