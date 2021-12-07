from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World.")


def detail(request, question_id):
    return HttpResponse("You're Looking the question: %s\n" % question_id)


def result(request, question_id):
    response = "You're Looking the question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're Looking the question." % question_id)