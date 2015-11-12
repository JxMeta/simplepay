# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0008_auto_20151111_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='home_display',
            field=models.BooleanField(default=False, verbose_name='Home'),
        ),
        migrations.AddField(
            model_name='tag',
            name='nav_display',
            field=models.BooleanField(default=False, verbose_name='Navigate'),
        ),
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.CharField(unique=True, max_length=256, verbose_name='Link'),
        ),
    ]
