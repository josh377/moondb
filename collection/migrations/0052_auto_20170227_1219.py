# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0051_userdetails_sevencpoints'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='checkid',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='sends',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='sevencpoints',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='sevencsends',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
    ]
