# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_questionsubtopic_subtopic_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('difficulty_level', models.IntegerField(default=0)),
                ('solution', models.CharField(max_length=200)),
                ('num_of_times_asked', models.IntegerField(default=0)),
                ('num_of_times_answered', models.IntegerField(default=0)),
                ('comments', models.CharField(max_length=200)),
                ('reviewer_votes', models.IntegerField(default=0)),
                ('answer_ratings', models.CharField(max_length=1, choices=[(b'1', b'Not Answered'), (b'2', b'Bad'), (b'3', b'Satisfactory'), (b'4', b'Good'), (b'5', b'Excellent')])),
                ('created_at', models.DateTimeField(verbose_name=b'created at')),
                ('sub_topic', models.ForeignKey(default=None, to='myapp.QuestionTopic')),
            ],
        ),
        migrations.RemoveField(
            model_name='questionsubtopic',
            name='answer_ratings',
        ),
        migrations.RemoveField(
            model_name='questionsubtopic',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='questionsubtopic',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='questionsubtopic',
            name='difficulty_level',
        ),
        migrations.RemoveField(
            model_name='questionsubtopic',
            name='num_of_times_answered',
        ),
        migrations.RemoveField(
            model_name='questionsubtopic',
            name='num_of_times_asked',
        ),
        migrations.RemoveField(
            model_name='questionsubtopic',
            name='question_text',
        ),
        migrations.RemoveField(
            model_name='questionsubtopic',
            name='reviewer_votes',
        ),
        migrations.RemoveField(
            model_name='questionsubtopic',
            name='solution',
        ),
    ]
