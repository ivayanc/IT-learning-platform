from django.views.generic.list import ListView
from .models import Post, ItPost, SchoolPost, ProgrammingPost
from django.shortcuts import render, redirect


class PostsView(ListView):
    model = Post
    paginate_by = 9
    context_object_name = 'posts'
    template_name = 'materials_system/posts.html'


class ItPostView(ListView):
    model = ItPost
    paginate_by = 9
    context_object_name = 'posts'
    template_name = 'materials_system/it.html'


class ProgrammingPostView(ListView):
    model = ProgrammingPost
    paginate_by = 9
    context_object_name = 'posts'
    template_name = 'materials_system/programming.html'

class SchoolPostView(ListView):
    model = SchoolPost
    paginate_by = 9
    context_object_name = 'posts'
    template_name = 'materials_system/school.html'