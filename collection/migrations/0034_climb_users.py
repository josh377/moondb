# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 02:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0033_auto_20170224_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='climb',
            name='users',
            field=models.ManyToManyField(through='collection.UserLog', to=settings.AUTH_USER_MODEL),
        ),
    ]
