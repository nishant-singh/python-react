# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques_id', models.IntegerField()),
                ('statement', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=300)),
                ('op2', models.CharField(max_length=300)),
                ('op3', models.CharField(max_length=300)),
                ('op4', models.CharField(max_length=300)),
            ],
        ),
    ]
