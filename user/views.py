from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
#from .models import User
from .models import Profile


def user(request):
    #todo
    # return all user here
    if request.method=='GET':
        data = {}
        try:
            user_db_data = User.objects.all()
            for user in user_db_data:
                data.update({"username": user.username, "email": user.email})
                # data["username"] = user.username

        except ObjectDoesNotExist:

            user_db_data = None

        return HttpResponse(json.dumps(data))


def profile(request):
    # all python code come here
    #todo
    # show particular user profile
    # get request
    if request.method == 'GET':
        user_id = request.GET.get("user_id")
        user = User.objects.get(id=user_id)
        profile = Profile.objects.get(user=user)
        data = {}
        for pf in profile:
            data.update({"first_name": pf.first_name,})
        return HttpResponse(json.dumps(data))




