from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField


class User(AbstractUser):
    country = CountryField(blank_label='(select country)')
    is_archived = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

