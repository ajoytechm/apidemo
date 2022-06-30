
from django.contrib import admin
from django.urls import path, include
# from .views import user, profile
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    # path('', user),
    path('', include(router.urls)),
    # path('profile/<user_id>', profile)

]
