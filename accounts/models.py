from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    country = CountryField(blank_label='(select country)')
    is_archived = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    class Status(models.TextChoices):
        UNREAD = 'UNRD', _('Unread Messages')
        READ = 'RD', _('Read Messages')
        ACCOUNT_CREATED = 'AC', _('Account created')
    name = models.CharField(max_length=250)
    email = models.EmailField()
    username = models.CharField(max_length=250)
    message = models.TextField()
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.UNREAD)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
