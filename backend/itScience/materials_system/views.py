from django.views.generic import ListView, DetailView
from .models import Post, ItPost, SchoolPost, ProgrammingPost, ScratchPost
from django.shortcuts import render, redirect


class SinglePostView(DetailView):
    template_name = 'materials_system/post_page.html'
    queryset = Post.objects.all()

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

class ScratchPostView(ListView):
    model = ScratchPost
    paginate_by = 9
    context_object_name = 'posts'
    template_name = 'materials_system/scratch.html'
