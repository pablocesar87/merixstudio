# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-20 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comment_count',
            field=models.IntegerField(blank=True, default=2),
        ),
    ]