# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=300)),
                ('lattitude', models.CharField(blank=True, max_length=20)),
                ('longitude', models.CharField(blank=True, max_length=20)),
                ('is_deleted', models.BooleanField(verbose_name='deleted', default=False)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'db_table': 'city',
            },
        ),
    ]
