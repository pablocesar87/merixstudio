# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-15 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160915_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='comment_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
