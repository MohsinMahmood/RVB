# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-10 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_p_d_l'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='OwnerID',
            field=models.CharField(default='00000', max_length=20),
        ),
        migrations.AddField(
            model_name='manager',
            name='TeamLeaderID',
            field=models.CharField(default='00000', max_length=20),
        ),
    ]
