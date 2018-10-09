# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0002_auto_20170413_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_time', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(default='no comment')),
                ('name', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]