"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from myapp import views
urlpatterns = [
    url(r'^dashboard/', views.view_dashboard, name="view_dashboard"),
    url(r'^question/', views.questions_list, name="view_questions_list"),
    url(r'^add_question_response/(?P<qid>[0-9]+)', views.add_question_response,
        name="add_question_response"),

    url(r'^view_question_response/(?P<qid>[0-9]+)',
        views.view_question_response, name="view_question_response"),
    url(r'^view_question_responses/(?P<qid>[0-9]+)',
        views.view_question_responses, name="view_question_responses"),
    url(r'^save_response/(?P<qid>[0-9]+)', views.save_response,
        name="save_response"),

    url(r'^perform_review/', views.perform_review,
        name="perform_review"),

    url(r'^view_start_review/(?P<review_id>[0-9]+)', views.view_start_review,
        name="view_start_review"),

    url(r'^view_my_reviews/', views.view_my_reviews,
        name="view_my_reviews"),

    url(r'^view_all_reviews/', views.view_all_reviews,
        name="view_all_reviews"),

    url(r'^candidate_review/(?P<review_id>[0-9]+)', views.view_candidate_review,
        name="view_candidate_review"),

    url(r'^freeze_review/', views.freeze_review,
        name="freeze_review"),

    url(r'^view_login/', views.view_login, name='view_login'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^signup/', views.user_signup, name='signup'),

    url(r'^admin/', include(admin.site.urls)),
]
