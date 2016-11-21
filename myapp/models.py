from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class QuestionTopic(models.Model):
    """ This would represent Major Topics for Questions """

    topic_text = models.CharField(max_length=200)
    additional_info = models.CharField(max_length=200)

    def __str__(self):
        return self.topic_text


class QuestionSubTopic(models.Model):
    """ This would keep track of sub Topics inside Major Topics """

    topic = models.ForeignKey(QuestionTopic, default=None)
    subtopic_text = models.CharField(max_length=200, default="NA")

    def __str__(self):
        return self.subtopic_text


class Question(models.Model):
    """ This would represent Questions """

    sub_topic = models.ForeignKey(QuestionSubTopic, default=None)
    question_text = models.CharField(max_length=200)
    difficulty_level = models.IntegerField(default=0)
    solution = models.CharField(max_length=200)

    num_of_times_asked = models.IntegerField(default=0)
    num_of_times_answered = models.IntegerField(default=0)
    reviewer_votes = models.IntegerField(default=0)
    created_at = models.DateTimeField('created at')

    def __str__(self):
        return self.question_text


class CandidateProfile(models.Model):

    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Interview(models.Model):

    candidate = models.ForeignKey(CandidateProfile, default=None)
    user = models.ForeignKey(User, default=None)
    status = models.CharField(max_length=20, default="Open")
    created_at = models.DateTimeField('created at', default=timezone.now())

    def __str__(self):
        return str(self.id)

class QuestionResponse(models.Model):
    """ This would represent Question Response """

    RATINGS = (
        ('1', 'Not Answered'),
        ('2', 'Bad'),
        ('3', 'Satisfactory'),
        ('4', 'Good'),
        ('5', 'Excellent'),
    )

    question = models.ForeignKey(Question, default=True)
    interview = models.ForeignKey(Interview, null=True)

    comments = models.CharField(max_length=500)
    answer_ratings = models.CharField(max_length=1, choices=RATINGS)
    response_given_by = models.CharField(max_length=50, default="NA")
    response_at = models.DateTimeField('response at', default=timezone.now())


