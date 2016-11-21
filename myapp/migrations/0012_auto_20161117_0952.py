# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20161114_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 17, 9, 52, 11, 922556, tzinfo=utc), verbose_name=b'created at'),
        ),
        migrations.AlterField(
            model_name='questionresponse',
            name='response_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 17, 9, 52, 11, 923213, tzinfo=utc), verbose_name=b'response at'),
        ),
    ]
