from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render, redirect


class SinglePostView(DetailView):
    template_name = 'materials_system/post_page.html'
    queryset = Post.objects.all()

class PostView(ListView):
    model = Post
    paginate_by = 9
    context_object_name = 'posts'
         
    template_name = 'materials_system/it.html'


class ItPostView(ListView):
    model = Post
    paginate_by = 9
    context_object_name = 'posts'

    def get_queryset(self):
         return Post.objects.filter(category=Post.IT)
         
    template_name = 'materials_system/it.html'


class ProgrammingPostView(ListView):
    model = Post
    paginate_by = 9
    context_object_name = 'posts'

    def get_queryset(self):
         return Post.objects.filter(category=Post.PROGRAMMING)
         
    template_name = 'materials_system/programming.html'

class SchoolPostView(ListView):
    model = Post
    paginate_by = 9
    context_object_name = 'posts'

    def get_queryset(self):
         return Post.objects.filter(category=Post.SCHOOL)
         
    template_name = 'materials_system/school.html'

class ScratchPostView(ListView):
    model = Post
    paginate_by = 9
    context_object_name = 'posts'

    def get_queryset(self):
         return Post.objects.filter(category=Post.SCRATCH)
         
    template_name = 'materials_system/scratch.html'