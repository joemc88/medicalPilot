# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20170808_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
        migrations.AddField(
            model_name='patient',
            name='address_line_one',
            field=models.CharField(default='1 abc street', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='address_line_three',
            field=models.CharField(default='townville', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='address_line_two',
            field=models.CharField(default='Ireland', max_length=100),
            preserve_default=False,
        ),
    ]