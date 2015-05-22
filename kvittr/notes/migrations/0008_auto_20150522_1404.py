# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0001_initial'),
        ('notes', '0007_auto_20150522_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='created_by',
        ),
        migrations.AddField(
            model_name='note',
            name='author',
            field=models.OneToOneField(default=0, to='useraccounts.Member'),
            preserve_default=False,
        ),
    ]
