# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-02 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0056_auto_20170301_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='eightaplussendsmonth',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='eightasendsmonth',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='eightbsendsmonth',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='sevenaplussendsmonth',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='sevenasendsmonth',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='sevenbplussendsmonth',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='sevenbsendsmonth',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='sevencplussendsmonth',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='sevencsendsmonth',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='sixbplussendsmonth',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='sixcplussendsmonth',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='sixcsendsmonth',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
    ]