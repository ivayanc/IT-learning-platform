from django.contrib import admin
from .models import Post, ItPost, ProgrammingPost, SchoolPost

admin.site.register(Post)
admin.site.register(SchoolPost)
admin.site.register(ItPost)
admin.site.register(ProgrammingPost)