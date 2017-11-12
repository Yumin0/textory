# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-11 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_auto_20171108_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='story',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='story.Tag'),
        ),
    ]
