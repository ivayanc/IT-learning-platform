from django.db import models
from django.contrib.auth.models import AbstractUser


class SystemUser(AbstractUser):
    name = models.CharField(max_length=200)
    about = models.TextField()