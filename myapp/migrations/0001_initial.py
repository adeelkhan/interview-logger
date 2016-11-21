# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionSubTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('difficulty_level', models.IntegerField(default=0)),
                ('solution', models.CharField(max_length=200)),
                ('num_of_times_asked', models.IntegerField(default=0)),
                ('num_of_times_answered', models.IntegerField(default=0)),
                ('comments', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('answer_ratings', models.CharField(max_length=1, choices=[(b'1', b'Not Answered'), (b'2', b'Bad'), (b'3', b'Satisfactory'), (b'4', b'Good'), (b'5', b'Excellent')])),
                ('created_at', models.DateTimeField(verbose_name=b'created at')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic_text', models.CharField(max_length=200)),
                ('additional_info', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='questionsubtopic',
            name='question',
            field=models.ForeignKey(to='myapp.QuestionTopic'),
        ),
    ]
