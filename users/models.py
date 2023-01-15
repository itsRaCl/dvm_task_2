from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    QuizMaster = models.BooleanField(default=False)
