
from django.contrib import admin
from django.urls import path
from .views import user, profile


urlpatterns = [
    path('', user),
    path('profile/<user_id>', profile) # 1

]
