# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20151111_1034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={},
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Tag Name'),
        ),
    ]
