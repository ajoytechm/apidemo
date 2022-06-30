from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .serializers import *

# Create your views here.
from rest_framework import viewsets, permissions


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


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = []

