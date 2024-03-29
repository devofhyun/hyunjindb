# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-15 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0015_auto_20180515_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inter',
            name='inter_apporve_num',
        ),
        migrations.RemoveField(
            model_name='mrapply',
            name='mr_apporve_num',
        ),
        migrations.AddField(
            model_name='company_info',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company_info',
            name='company_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Member_info'),
        ),
        migrations.AlterField(
            model_name='company_info',
            name='jobcode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Occupation_type'),
        ),
        migrations.AlterField(
            model_name='mento_info',
            name='mento_career',
            field=models.CharField(max_length=3),
        ),
    ]
