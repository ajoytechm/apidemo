from django.contrib import admin
from django.urls import path
from .views import profile,user


urlpatterns = [
    #path('', user),
    path('',user),
    path('profile', profile) # 1

]