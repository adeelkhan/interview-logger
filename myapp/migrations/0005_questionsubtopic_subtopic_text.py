# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20161109_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionsubtopic',
            name='subtopic_text',
            field=models.CharField(default=b'NA', max_length=200),
        ),
    ]
