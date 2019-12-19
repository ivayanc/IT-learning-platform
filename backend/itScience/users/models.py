from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser


class SystemUser(AbstractUser):
    name = models.CharField(max_length=200, verbose_name="Ім'я")
    about = models.TextField(verbose_name="Про себе")
    avatar = models.ImageField(upload_to='avatars/',verbose_name="Ваше фото",default="avatars/default-avatar.png")
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse("profile", kwargs={"id": self.pk})
    

   