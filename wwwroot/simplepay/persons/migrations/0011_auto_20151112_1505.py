# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0010_auto_20151112_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'Persons'},
        ),
        migrations.RemoveField(
            model_name='person',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='slug',
        ),
    ]
