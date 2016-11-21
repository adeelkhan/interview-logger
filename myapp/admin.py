from django.contrib import admin

# Register your models here.

from .models import  QuestionTopic
from .models import QuestionSubTopic
from .models import Question
from .models import QuestionResponse
from .models import CandidateProfile
from .models import Interview


# registering models
admin.site.register(QuestionTopic)
admin.site.register(QuestionSubTopic)
admin.site.register(Question)
admin.site.register(QuestionResponse)
admin.site.register(CandidateProfile)
admin.site.register(Interview)



