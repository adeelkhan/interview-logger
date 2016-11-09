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
    url(r'^dashboard/', views.dashboard, name="view_dashboard"),
    url(r'^question/', views.questions_list, name="view_questions_list"),
    url(r'^question_response/(?P<qid>[0-9]+)', views.question_response, name="question_response"),
    url(r'^admin/', include(admin.site.urls)),
]
