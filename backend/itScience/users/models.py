from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    role_name = models.CharField(max_length=200, verbose_name="Назва ролi")
    can_post = models.BooleanField(default=False, verbose_name="Може публiкувати статтi")
    can_edit_posts = models.BooleanField(default=False, verbose_name="Може редагувати чужi статтi")
    can_change_hashtags = models.BooleanField(default=False, verbose_name="Можливicть редагувати та додавати хештеги")
    can_edit_users = models.BooleanField(default=False, verbose_name="Можливicть редагування користувачiв")

    def __str__(self):
        return self.role_name

class SystemUser(AbstractUser):
    name = models.CharField(max_length=200, verbose_name="Ім'я")
    stydy_class = models.IntegerField(verbose_name="Клас навчанн", blank=True, default=9)
    about = models.TextField(verbose_name="Про себе")
    avatar = models.ImageField(upload_to='avatars/',verbose_name="Ваше фото",default="avatars/default-avatar.png")
    google_avatar = models.CharField(max_length=250, verbose_name="Google avatar", default="")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True, default=2)
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse("profile", kwargs={"id": self.pk})
