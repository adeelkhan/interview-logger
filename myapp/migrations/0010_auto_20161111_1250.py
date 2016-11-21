# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0009_auto_20161110_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('candidate', models.ForeignKey(default=None, to='myapp.CandidateProfile')),
                ('user', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='questionresponse',
            name='question',
            field=models.ForeignKey(default=True, to='myapp.Question'),
        ),
        migrations.AlterField(
            model_name='questionresponse',
            name='response_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 11, 12, 50, 41, 738299, tzinfo=utc), verbose_name=b'response at'),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='interview',
            field=models.ForeignKey(to='myapp.Interview', null=True),
        ),
    ]
