# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20161109_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='response_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 10, 7, 43, 20, 572224, tzinfo=utc), verbose_name=b'response at'),
        ),
        migrations.AddField(
            model_name='question',
            name='response_given_by',
            field=models.CharField(default=b'NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='comments',
            field=models.CharField(max_length=500),
        ),
    ]
