# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 23:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0006_climb_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='climb',
            name='added_by',
        ),
    ]