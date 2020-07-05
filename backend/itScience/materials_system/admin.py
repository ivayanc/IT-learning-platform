from django.contrib import admin
from .models import Post, HashTag, PostHashTag


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
    list_display = ('category', 'title', 'moderator', 'time_to_read')
    filter_list = ('category', 'moderator',)

@admin.register(HashTag)
class HashTags(admin.ModelAdmin):
    fields = (
    'tag_name',
    'tag_parent',
    'tag_main',)
    list_display = ('tag_name', 'tag_parent', 'tag_main')
    filter_list = ('tag_parent', 'tag_main')

@admin.register(PostHashTag)
class HashTags(admin.ModelAdmin):
    fields = (
    'post',
    'tag',)
    list_display = ('post', 'tag')
    filter_list = ('tag')
