# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20150515_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 5, 15, 7, 59, 31, 363118, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
