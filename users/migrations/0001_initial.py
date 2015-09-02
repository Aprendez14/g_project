# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('description', models.TextField(default=b'No description', max_length=300)),
                ('consequence', models.TextField(max_length=300)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('golden_badges', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('silver_badges', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('bronze_badges', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('points', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('level', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('percent_in_level', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
