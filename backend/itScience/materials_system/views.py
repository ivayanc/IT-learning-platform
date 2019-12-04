from django.views.generic.list import ListView
from .models import Post
from django.shortcuts import render, redirect

class PostsView(ListView):
    model = Post
    paginate_by = 5
    context_object_name = 'posts'
    template_name = 'materials_system/posts.html'

    def get_queryset(self):
        category = self.request.GET.get('category', 'it')
        new_context = Post.objects.filter(
            category=category,
        )
        return new_context

    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)
        context['category'] = self.request.GET.get('category', 'it')
        return context

