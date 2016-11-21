from django.shortcuts import render
from .models import QuestionTopic, QuestionSubTopic, Question
from .models import QuestionResponse
from .models import CandidateProfile
from .models import Interview
from django.utils import timezone

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.core.urlresolvers import reverse


@login_required(login_url="/view_login")
def perform_review(request):
    """
    Initiate the interview process. Do initializations for interview and
    necessary checks to avoid multiple interview generations for a
    candidate.

    :param request: http request object
            qid: question id for the question selected by user
    :return None:

    """

    cid = request.POST.get("candidate_id")
    print "candidate id " + str(cid)

    # test here if the (reviewer, candidate) tuple is not already there
    # and its a new interview

    interview = None
    if Interview.objects.all().exists():
        try:
            interview = Interview.objects.get(candidate_id=cid,
                                                user_id=request.user.id)

            candidate_list = CandidateProfile.objects.all()
            candidate = CandidateProfile.objects.get(id=cid)

            dict = {}
            dict["candidate_list"] = candidate_list
            dict["candidate"] = candidate
            dict["review_status"] = "open"

            # review closed go the dashboard for new review otherwise
            # continue with the existing review

            if interview.status == "closed":
                dict["review_status"] = "closed"
                return render(request, 'myapp/dashboard.html', dict)
            else:
                return HttpResponseRedirect(
                    reverse('view_start_review', args=(),
                            kwargs={'review_id': interview.id}))

        except Interview.DoesNotExist:
            interview = Interview.objects.create(candidate_id=cid,
                                                 user_id=request.user.id,
                                                 status="open")
    else:
        interview = Interview.objects.create(candidate_id=cid,
                                                user_id=request.user.id,
                                                status="open")

    return HttpResponseRedirect(reverse('view_start_review', args=(),
                                        kwargs={'review_id': interview.id}))


def freeze_review(request):
    """
    Enable user to freeze an interview. User can further give
    ask questions for that specific interview

    :param request: http request object
    :return None:

      """
    review_id = request.GET.get("review_id")
    review = Interview.objects.get(id=review_id)
    review.status = "closed"
    review.save()

    candidate_list = CandidateProfile.objects.all()

    return render(request, 'myapp/dashboard.html', {
        'candidate_list': candidate_list
    })


@login_required(login_url="/view_login")
def view_start_review(request, review_id):
    """
    Enable user to view dashboard. Handles both functionality of listing
    topics and subtopics

    :param request:
    :return None:

    """

    print review_id
    interview = Interview.objects.get(id = review_id)
    candidate = CandidateProfile.objects.get(id=interview.candidate_id)

    dict = {}

    dict['candidate'] = candidate
    dict['review_id'] = review_id

    # first time accessing list only Topics
    if request.POST.get("topic") is None:
        topics = QuestionTopic.objects.all()
        dict['topics_list'] = topics
        dict['sub_topic'] = False

    else:
        # list both topics and subtopics
        topics = QuestionTopic.objects.all()
        dict['topics_list'] = topics

        topic_id = request.POST.get("topic")
        topic = QuestionTopic.objects.get(id=topic_id)
        sub_topic_list = topic.questionsubtopic_set.all()

        dict['sub_topics_list'] = sub_topic_list
        dict['sub_topic'] = True

    return render(request, 'myapp/start_review.html', dict)

def view_my_reviews(request):
    """
    Enable user to view his/her reviews for a candidate

    :param request:
    :return None:

    """
    review_list = Interview.objects.filter(user_id=request.user.id)
    print review_list
    return render(request, 'myapp/review_list.html', {
        'review_list': review_list,
        'show_reviews': 'personal'
    })


def view_candidate_review(request, review_id):
    """
    Enable user to view a specific review of a candidate

    :param request: http request object
         review_id : Interview id for that candidate
    :return None:

    """

    rating_choice = ['',
                     'Not Answered',
                     'Bad',
                     'Satisfactory',
                     'Good',
                     'Excellent'
                     ]
    review = Interview.objects.get(id=review_id)
    review_responses = review.questionresponse_set.all()

    print review_responses
    return render(request, 'myapp/candidate_review.html', {
        'review_responses': review_responses,
        'candidate_name': review.candidate.name,
        'reviewer_name' : review.user.username,
        'ratings': rating_choice
    })

def view_all_reviews(request):

    """
    Enable user to list of all interviews conducted by him/her

    :param request: http request object
    :return None:

    """
    review_list = Interview.objects.all()

    return render(request, 'myapp/review_list.html', {
        'review_list': review_list,
        'show_reviews': 'all'
    })

@login_required(login_url="/view_login")
def questions_list(request):
    """
    Enable user to view questions for a sub topic as a list.

    :param request:
    :return None:

    """

    dict = {}

    sub_topic_id=0
    if request.POST.get("sub_topic") is not None:
        sub_topic_id = request.POST.get("sub_topic")
    elif request.GET.get("sub_topic") is not None:
        sub_topic_id = request.GET.get("sub_topic")

    review_id=0
    if request.POST.get("review_id") is not None:
        review_id = request.POST.get("review_id")
    elif request.GET.get("review_id") is not None:
        review_id = request.GET.get("review_id")

    difficulty_level = request.POST.get("difficulty_level")

    # Show all when no difficulty filter applied
    if difficulty_level is None or \
                    int(difficulty_level) is 4:
        question_list = Question.objects.filter(
            sub_topic_id=sub_topic_id) \
            .order_by('-num_of_times_asked')

    # apply a filter based on difficulty
    else:
        question_list = Question.objects.filter(
            sub_topic_id=sub_topic_id,
            difficulty_level=difficulty_level
        ).order_by('-num_of_times_asked')


    already_responded_list = QuestionResponse.objects.\
                                filter(interview_id=review_id)
    interview = Interview.objects.get(id=review_id)
    candidate = interview.candidate

    dict["question_list"] = question_list
    dict["already_responded_list"] = already_responded_list
    dict["sub_topic"] = sub_topic_id
    dict['review_id'] = review_id
    dict["candidate"] = candidate

    return render(request, 'myapp/questions.html', dict)

@login_required(login_url="/view_login")
def add_question_response(request, qid):
    """
    Enable user to view response page for a question

    :param request: http request object
            qid: question id for the question selected by user
    :return None:

    """

    dict = {}
    question = Question.objects.get(id=qid)
    review_id = request.GET.get("review_id")
    candidate = Interview.objects.get(id=review_id).candidate

    dict['review_id'] = review_id
    dict["question"] = question
    dict["sub_topic"] = question.sub_topic.id
    dict['candidate'] = candidate

    return render(request, 'myapp/question_response.html', dict)


@login_required(login_url="/view_login")
def save_response(request, qid):
    """
    Enable user to save his/her response for a question

    :param request: http request object
            qid: question id for the question selected by user
    :return None:

    """

    rating_choice = {
        'Not Answered': 1,
        'Bad': 2,
        'Satisfactory': 3,
        'Good': 4,
        'Excellent': 5
    }

    dict = {}
    rating = request.POST.get("ratings")
    comments = request.POST.get("comments")
    review_id = request.POST.get("review_id")

    question = Question.objects.get(id=qid)
    sub_topic_id = question.sub_topic.id

    candidate= Interview.objects.get(id=review_id).candidate

    # if response not existed for this question and interview then add it
    try:
        QuestionResponse.objects.get(question_id=qid,
                                        interview_id=review_id)
        dict['response_saved'] = False

    except QuestionResponse.DoesNotExist:

        question_response = QuestionResponse(question_id = qid,
                                             answer_ratings=int(rating),
                                             response_at=timezone.now(),
                                             response_given_by=request.user.username,
                                             comments=comments)

        if int(rating) is not rating_choice['Not Answered']:
            question.num_of_times_answered += 1
        question.num_of_times_asked += 1

        question_response.interview_id = review_id
        question_response.save()
        question.save()

        dict['response_saved'] = True

    question_list = Question.objects.filter(sub_topic_id=sub_topic_id). \
        order_by('-num_of_times_asked')
    already_responded_list = QuestionResponse.objects.\
                                filter(interview_id=review_id)

    dict['sub_topic'] = sub_topic_id
    dict['review_id'] = review_id
    dict['question_list'] = question_list
    dict["already_responded_list"] = already_responded_list
    dict['candidate'] = candidate

    return render(request, 'myapp/questions.html', dict)

@login_required(login_url="/view_login")
def view_question_response(request, qid):
    """
    Enable user to view his/her question response

    :param request: http request object
            qid: question id for the question selected by user
    :return None:

    """

    rating_choice = ['',
                     'Not Answered',
                     'Bad',
                     'Satisfactory',
                     'Good',
                     'Excellent'
                     ]

    review_id = request.GET.get("review_id")
    response = QuestionResponse.objects.get(question_id=qid,
                                            interview_id=review_id)
    dict = {}

    dict["question"] = response.question
    dict["sub_topic"] = response.question.sub_topic.id
    dict['ratings'] = rating_choice
    dict['review_id'] = request.GET.get("review_id")
    dict['response'] = response

    return render(request, 'myapp/view_question_response.html', dict)

@login_required(login_url="/view_login")
def view_question_responses(request, qid):
    """
    Enable user to view all responses for a question

    :param request: http request object
            qid: question id for the question selected by user
    :return None:

    """

    sub_topic_id = request.GET.get("sub_topic")
    review_id = request.GET.get("review_id")

    rating_choice = ['',
                     'Not Answered',
                     'Bad',
                     'Satisfactory',
                     'Good',
                     'Excellent'
                     ]
    question_responses = QuestionResponse.objects.filter(question_id=qid)

    dict = {}
    q = Question.objects.get(id = qid)

    dict['ratings'] = rating_choice
    dict["question_response_list"] = question_responses
    dict["sub_topic"] = sub_topic_id
    dict["review_id"] = review_id

    return render(request, 'myapp/view_question_responses.html', dict)

@login_required(login_url="/view_login")
def view_dashboard(request):
    """
    Enable user to view dashboard page

    :param request: request object having values
    :return None:
    """
    candidate_list = CandidateProfile.objects.all()

    return render(request, 'myapp/dashboard.html', {
        'candidate_list': candidate_list
    })

def view_login(request):
    """
    Enable user to view login page

    :param request: request object having values
    :return None:
    """

    return render_to_response('myapp/view_login.html', {},
                              RequestContext(request))

def user_login(request):
    """
    This view authenticate user for a username, password

    :param request: request object having values
    :return None:
    """

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'myapp/logout.html', {})

    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'my_app/view_login.html', {})


@login_required(login_url="/view_login")
def user_logout(request):
    """
    Enable user to logout from app

    :param request: request object having values
    :return None:
    """
    logout(request)
    # Take the user back to login.
    return HttpResponseRedirect('/view_login/')

def user_signup(request):
    """
    Enable user signup to app

    :param request: request object having values
    :return None:
    """
    # todo not implemented yet

    return HttpResponse("signup.")


