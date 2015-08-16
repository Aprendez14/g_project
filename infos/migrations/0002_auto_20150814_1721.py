# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='bronze_badges',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='golden_badges',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='level',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='percent_in_level',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='points',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='silver_badges',
            field=models.PositiveIntegerField(),
        ),
    ]
