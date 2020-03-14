from django.db import models
import datetime as dt
from django .contrib.auth.models import User
from tinymce.modes import HTMLField
from django.db.models.signals import post save
from django.dispatch import receiver


class Profile(models.Model):
    