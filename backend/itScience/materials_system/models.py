from django.db import models

from users.models import SystemUser

class UserInfo(models.Model):
    #user = models.OneToOneField(User)
    name = models.CharField(max_length=255)
    about = models.CharField(max_length=500)

class Post(models.Model):
    moderator = models.ForeignKey(SystemUser,on_delete=models.CASCADE)
    author = models.CharField(max_length=255,blank=True)
    title = models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=500,blank=True)
    published = models.DateTimeField(auto_now=True,blank=True)
    title_image = models.ImageField(upload_to='static/post_images/',blank=True)
    publication = models.TextField()

class ItPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

class SchoolPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

class ProgrammingPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

class HashTag(models.Model):
    tag_name = models.CharField(max_length=50)

class PostHashTag(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    tag = models.ForeignKey(HashTag,on_delete=models.CASCADE)


