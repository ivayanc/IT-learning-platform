from django.db import models

from users.models import SystemUser

class Post(models.Model):

    PROGRAMMING = 1
    SCHOOL = 2
    IT = 3
    SCRATCH = 4
    OTHER  = 5
    CATEGORY_CHOICES = [
        (PROGRAMMING, ('Програмування')),
        (SCHOOL, ('Шкільна інформатика')),
        (IT, ('Інформаційні технології')),
        (SCRATCH, ('Scratch')),
        (OTHER, ('Стаття')),
    ]

    time_to_read     = models.CharField(max_length=20,verbose_name="Прочитаєте за")
    moderator        = models.ForeignKey(SystemUser,on_delete=models.CASCADE,verbose_name="Автор")
    title            = models.CharField(max_length=255,blank=True,verbose_name="Заголовок")
    views            = models.IntegerField(default=0,verbose_name="Кількість переглядів")
    description      = models.CharField(max_length=500,blank=True, verbose_name="Короткий опис")
    published        = models.DateTimeField(auto_now=True,blank=True,verbose_name="Дата публікації")
    title_image      = models.ImageField(upload_to="posts",blank=True, verbose_name="Зображення",default="posts/default.png")
    publication      = models.TextField(verbose_name="Текст публікації")
    favorites       = models.ManyToManyField(SystemUser, related_name="Обрані", blank=True)
    likes            = models.ManyToManyField(SystemUser, related_name="Лайки", blank=True)
    category         = models.PositiveSmallIntegerField(
                            choices = CATEGORY_CHOICES,
                            default = OTHER,
    )

class HashTag(models.Model):
    tag_name = models.CharField(max_length=50)

class PostHashTag(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    tag = models.ForeignKey(HashTag,on_delete=models.CASCADE)


