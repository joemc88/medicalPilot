# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 14:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAdmin', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('form', '0006_auto_20170808_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackPain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Inspection', models.CharField(max_length=250)),
                ('Palpatation', models.CharField(max_length=250)),
                ('Range_PainOnMovement', models.CharField(max_length=250)),
                ('SLR_Right', models.CharField(max_length=250)),
                ('Tone_Left', models.CharField(max_length=250)),
                ('Tone_Right', models.CharField(max_length=250)),
                ('Hip_Flexion_Left', models.CharField(max_length=250)),
                ('Hip_Flexion_Right', models.CharField(max_length=250)),
                ('Knee_Extension_Left', models.CharField(max_length=250)),
                ('Knee_Extension_Right', models.CharField(max_length=250)),
                ('Knee_Flexion_Left', models.CharField(max_length=250)),
                ('Knee_Flexion_Right', models.CharField(max_length=250)),
                ('Ankle_Dorsi_Flexion_Left', models.CharField(max_length=250)),
                ('Ankle_Dorsi_Flexion_Right', models.CharField(max_length=250)),
                ('Ankle_Plantar_Flexion_Left', models.CharField(max_length=250)),
                ('Ankle_Plantar_Flexion_Right', models.CharField(max_length=250)),
                ('Extension_Hallicus_Longus_Left', models.CharField(max_length=250)),
                ('Extension_Hallicus_Longus_Right', models.CharField(max_length=250)),
                ('Coordination_Left', models.CharField(max_length=250)),
                ('Coordination_Right', models.CharField(max_length=250)),
                ('Sensation', models.CharField(max_length=250)),
                ('Reflex_Knee_Left', models.CharField(max_length=250)),
                ('Reflex_Knee_Right', models.CharField(max_length=250)),
                ('Reflex_Ankle_Left', models.CharField(max_length=250)),
                ('Reflex_Ankle_Right', models.CharField(max_length=250)),
                ('Reflex_Plantar_Left', models.CharField(max_length=250)),
                ('Reflex_Plantar_Right', models.CharField(max_length=250)),
                ('carriedOutBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='backpainInspector', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAdmin.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='LBPCharactarise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Location', models.CharField(max_length=250)),
                ('Radiation', models.CharField(max_length=250)),
                ('Duration', models.CharField(max_length=250)),
                ('Periodicity', models.CharField(max_length=250)),
                ('Character', models.CharField(max_length=250)),
                ('AggrivatingFactors', models.CharField(max_length=250)),
                ('RelievingFactors', models.CharField(max_length=250)),
                ('ASNumbness', models.BooleanField()),
                ('ASParaesthesia', models.BooleanField()),
                ('ASSyncope', models.BooleanField()),
                ('ASWeakness', models.BooleanField()),
                ('ASSphincterDisturbance', models.BooleanField()),
                ('ASDizziness', models.BooleanField()),
                ('ASOther', models.BooleanField()),
                ('ASOtherStated', models.CharField(max_length=250)),
                ('Interventions_Analgesia', models.CharField(max_length=250)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAdmin.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PainPerceptionDiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('PainAtWorst', models.IntegerField()),
                ('PainAtLeast', models.IntegerField()),
                ('PainOnAverage', models.IntegerField()),
                ('PainRightNow', models.IntegerField()),
                ('GeneralActivity', models.IntegerField()),
                ('Mood', models.IntegerField()),
                ('WalkingAbility', models.IntegerField()),
                ('NormalWork', models.IntegerField()),
                ('Relationships', models.IntegerField()),
                ('Sleep', models.IntegerField()),
                ('EnjoymentOfLife', models.IntegerField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAdmin.Patient')),
            ],
        ),
    ]