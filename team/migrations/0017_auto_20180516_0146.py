# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-15 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0016_auto_20180515_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='mrapply_num',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='team.Mrapply'),
            preserve_default=False,
        ),
    ]
