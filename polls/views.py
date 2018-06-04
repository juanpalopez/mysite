from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello, django. This is the polls index')


def detail(request, question_id):
    return HttpResponse("You're looking ate question %s" % question_id)


def results(request, question_id):
    response = HttpResponse("You're looking at results of question %i")
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
