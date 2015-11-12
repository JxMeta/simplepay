# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_auto_20151111_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='tag_list',
            new_name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.CharField(max_length=256, null=True, verbose_name='Tag Link', db_index=True),
        ),
    ]
