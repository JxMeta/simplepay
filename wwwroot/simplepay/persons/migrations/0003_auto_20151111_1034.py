# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20151111_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 10, 34, 27, 377976, tzinfo=utc), verbose_name='Publish Date', auto_now_add=True),
            preserve_default=False,
        ),
    ]
