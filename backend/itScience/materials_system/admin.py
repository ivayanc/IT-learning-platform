from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = (
    'category',
    'time_to_read',
    'moderator',
    'title',
    'views',
    'description',
    'title_image',
    'publication',)
