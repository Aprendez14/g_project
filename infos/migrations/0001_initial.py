# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('golden_badges', models.IntegerField()),
                ('silver_badges', models.IntegerField()),
                ('bronze_badges', models.IntegerField()),
                ('points', models.IntegerField()),
                ('level', models.IntegerField()),
                ('percent_in_level', models.IntegerField()),
                ('last_login', models.DateTimeField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
