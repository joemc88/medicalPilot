# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='recieved',
        ),
        migrations.AlterField(
            model_name='message',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
