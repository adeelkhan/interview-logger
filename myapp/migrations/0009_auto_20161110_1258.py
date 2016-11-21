# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20161110_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.CharField(max_length=500)),
                ('answer_ratings', models.CharField(max_length=1, choices=[(b'1', b'Not Answered'), (b'2', b'Bad'), (b'3', b'Satisfactory'), (b'4', b'Good'), (b'5', b'Excellent')])),
                ('response_given_by', models.CharField(default=b'NA', max_length=50)),
                ('response_at', models.DateTimeField(default=datetime.datetime(2016, 11, 10, 12, 58, 16, 620210, tzinfo=utc), verbose_name=b'response at')),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer_ratings',
        ),
        migrations.RemoveField(
            model_name='question',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='question',
            name='response_at',
        ),
        migrations.RemoveField(
            model_name='question',
            name='response_given_by',
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='question',
            field=models.ForeignKey(default=None, to='myapp.Question'),
        ),
    ]
