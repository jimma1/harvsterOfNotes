# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_auto_20150522_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='num_likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
