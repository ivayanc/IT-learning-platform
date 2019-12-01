from django.db import models


class UserInfo(models.Model):
    #user = Models.OneToOneField()

class Post(models.Model):
    moderator = models.ForeignKey(User,on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    short_title = models.CharField(max_length=150)
    full_title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    published = models.DateTimeField(auto_now=True)
    title_image = models.ImageField()
    

class HashTag(models.Model):
    pass
