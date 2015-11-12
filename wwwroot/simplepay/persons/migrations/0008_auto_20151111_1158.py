# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0007_auto_20151111_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.CharField(default=datetime.datetime(2015, 11, 11, 11, 58, 5, 569076, tzinfo=utc), max_length=256, verbose_name='Link', db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.CharField(default=datetime.datetime(2015, 11, 11, 11, 58, 14, 237972, tzinfo=utc), max_length=256, verbose_name='Tag Link', db_index=True),
            preserve_default=False,
        ),
    ]
