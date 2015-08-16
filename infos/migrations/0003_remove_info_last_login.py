# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0002_auto_20150814_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='last_login',
        ),
    ]
