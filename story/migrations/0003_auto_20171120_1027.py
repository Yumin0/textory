# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-20 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_auto_20171114_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='create_at',
        ),
        migrations.AlterField(
            model_name='story',
            name='sb_story',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
