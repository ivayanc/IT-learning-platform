from django.db import models
from django.urls import reverse
from django.conf import settings
from datetime import datetime    
from users.models import SystemUser

from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):

    time_to_read     = models.CharField(max_length=20,verbose_name="Прочитаєте за")
    moderator        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True,verbose_name="Автор")
    title            = models.TextField(blank=True,verbose_name="Заголовок", unique=False)
    views            = models.IntegerField(default=0,verbose_name="Кількість переглядів")
    description      = models.TextField(blank=True, verbose_name="Короткий опис")
    published        = models.DateTimeField(blank=True,verbose_name="Дата публікації", null = True, default=datetime.now)
    title_image      = models.ImageField(upload_to="posts",blank=True, verbose_name="Зображення",default="posts/default.png")
    publication      = RichTextUploadingField(verbose_name="Текст публікації")
    favorite         = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Обрані", blank=True)
    likes            = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Лайки", blank=True)   

    def get_absolute_url(self):
        return reverse("post-details", kwargs={"id": self.pk})
    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey(Post, verbose_name="Пост до якого написан комментар", on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор комментара", on_delete = models.CASCADE)
    text = models.CharField(max_length=200, verbose_name="Текст комментаря")
    date = models.DateTimeField(blank=True, verbose_name="Дата написання коментаря", null=True)
    reply_to = models.ForeignKey('self', on_delete = models.CASCADE, blank = True, null = True, verbose_name="Вiдповiдь на")

class HashTag(models.Model):
    tag_name = models.CharField(max_length=50)
    tag_parent = models.ForeignKey('self', on_delete = models.CASCADE, blank = True, null = True)
    tag_main = models.BooleanField(blank=False, default=False)
    page_photo = models.ImageField(upload_to="posts", blank = True, verbose_name="Зоображеня категорії", default="posts/alexandru-acea-XEB8y0nRRP4-unsplash.jpg")
    class Meta:
        unique_together = ("tag_name", "tag_parent")

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


