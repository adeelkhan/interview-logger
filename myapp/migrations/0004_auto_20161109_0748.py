# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20161109_0747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionsubtopic',
            old_name='question',
            new_name='question_text',
        ),
        migrations.AddField(
            model_name='questionsubtopic',
            name='topic',
            field=models.ForeignKey(default=None, to='myapp.QuestionTopic'),
        ),
    ]
