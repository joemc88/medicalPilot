# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_backpain_lbpcharactarise_painperceptiondiary'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LBPCharactarise',
            new_name='LBPCharacterise',
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
