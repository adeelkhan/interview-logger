# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20161111_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='status',
            field=models.CharField(default=b'Open', max_length=20),
        ),
        migrations.AlterField(
            model_name='questionresponse',
            name='response_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 14, 12, 57, 26, 498936, tzinfo=utc), verbose_name=b'response at'),
        ),
    ]
