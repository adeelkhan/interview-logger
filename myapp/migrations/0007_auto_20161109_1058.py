# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20161109_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='sub_topic',
            field=models.ForeignKey(default=None, to='myapp.QuestionSubTopic'),
        ),
    ]
