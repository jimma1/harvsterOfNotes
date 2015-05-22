# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_note_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_by',
            field=models.ForeignKey(to='useraccounts.Member'),
        ),
    ]
