from django.contrib import admin
from .models import Post, HashTag, PostHashTag, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = (
    'time_to_read',
    'moderator',
    'title',
    'views',
    'description',
    'title_image',
    'publication',
    'published',)
    list_display = ('title', 'moderator', 'time_to_read')
    filter_list = ('moderator',)

@admin.register(HashTag)
class HashTags(admin.ModelAdmin):
    fields = (
    'tag_name',
    'tag_parent',
    'tag_main',)
    list_display = ('tag_name', 'tag_parent', 'tag_main')
    filter_list = ('tag_parent', 'tag_main')

@admin.register(Comments)
class Comments(admin.ModelAdmin):
    fields = (
    'post',
    'user',
    'text',
    'date',)
    filter_list = ('post')

@admin.register(PostHashTag)
class HashTags(admin.ModelAdmin):
    fields = (
    'post',
    'tag',)
    list_display = ('post', 'tag')
    filter_list = ('tag')
