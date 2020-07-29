from django.db import models
from django.urls import reverse
from django.conf import settings

from users.models import SystemUser

from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):

    time_to_read     = models.CharField(max_length=20,verbose_name="Прочитаєте за")
    moderator        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name="Автор")
    title            = models.CharField(max_length=255,blank=True,verbose_name="Заголовок", unique=True)
    views            = models.IntegerField(default=0,verbose_name="Кількість переглядів")
    description      = models.CharField(max_length=500,blank=True, verbose_name="Короткий опис")
    published        = models.DateTimeField(auto_now=True,blank=True,verbose_name="Дата публікації")
    title_image      = models.ImageField(upload_to="posts",blank=True, verbose_name="Зображення",default="posts/default.png")
    publication      = RichTextUploadingField(verbose_name="Текст публікації")
    favorite         = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Обрані", blank=True)
    likes            = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Лайки", blank=True)   

    def get_absolute_url(self):
        return reverse("post-details", kwargs={"id": self.pk})
    def __str__(self):
        return self.title



class HashTag(models.Model):
    tag_name = models.CharField(max_length=50, unique=True)
    tag_parent = models.ForeignKey('self', on_delete = models.CASCADE, blank = True, null = True)
    tag_main = models.BooleanField(blank=False, default=False)
    
    def __str__(self):
        return self.tag_name
    
    def get_absolute_url(self):
        return reverse("hashtag-details", kwargs={"id": self.pk})

class PostHashTag(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    tag = models.ForeignKey(HashTag,on_delete=models.CASCADE)
    def __str__(self):
        return self.tag.tag_name
    class Meta:
        unique_together = ("post", "tag")


