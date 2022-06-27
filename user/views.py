from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def user(request):
    #todo
    # return all user here
    # this will be get request
    return HttpResponse("Hello, this is first django project")


def profile(request):
    # all python code come here
    #todo
    # show particular user profile
    # get request
    return HttpResponse("Hello, this is my profile")


