# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0002_auto_20180502_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_url', models.CharField(max_length=30)),
                ('v_tiems', models.IntegerField()),
            ],
            options={
                'db_table': 'visit',
            },
        ),
    ]
