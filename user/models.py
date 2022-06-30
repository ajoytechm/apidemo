from django.contrib.auth.models import User
from django.db import models


# class User(models.Model):   # user_users
#     # id  primary key of this model or table
#     # first_name = models.CharField(max_length=50, null=False)
#     # last_name = models.CharField(max_length=50, null=False)
#     username = models.CharField(max_length=32, blank=False, null=False, unique=True)
#     mobile = models.CharField(max_length=10, blank=True, null=True)
#     email = models.EmailField(max_length=100, null=False)


class Profile(models.Model):  # user_profiles
    # id
    user = models.ForeignKey(unique=True, on_delete=models.CASCADE, to=User)  # user_id
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)


