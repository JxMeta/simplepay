# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('sex', models.CharField(default='M', max_length=1, verbose_name='Gender', choices=[('M', 'Male'), ('F', 'Female')])),
                ('age', models.IntegerField(default=0, verbose_name='Age')),
                ('active', models.CharField(default='Y', max_length=1, verbose_name='Active', choices=[('Y', 'Yes'), ('N', 'No')])),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='tag name')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'tag',
                'verbose_name_plural': 'tag',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='tag_list',
            field=models.ManyToManyField(to='persons.Tag', verbose_name='Tag'),
        ),
    ]
