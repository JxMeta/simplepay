# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Publish Date', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Update Date', null=True),
        ),
    ]
