# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kintegrate',
            name='number',
            field=models.BigIntegerField(),
            preserve_default=True,
        ),
    ]
