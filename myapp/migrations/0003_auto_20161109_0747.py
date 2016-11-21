# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20161109_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsubtopic',
            name='question',
            field=models.CharField(max_length=200),
        ),
    ]
