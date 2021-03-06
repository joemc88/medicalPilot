# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=250)),
                ('had_pain', models.CharField(max_length=250)),
                ('when_started', models.CharField(max_length=250)),
                ('where_pain', models.CharField(max_length=250)),
                ('pain_frequency', models.CharField(max_length=250)),
                ('pain_duration', models.CharField(max_length=250)),
                ('medication', models.CharField(max_length=250)),
                ('medication_works', models.CharField(max_length=250)),
                ('life_disturbance', models.CharField(max_length=250)),
                ('sleep_disturbed', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('medical_card_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='formsubmission',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Patient'),
        ),
    ]
