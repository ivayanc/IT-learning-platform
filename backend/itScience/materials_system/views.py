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
    template_name = 'materials_system/posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = "Статті"
        context['category_description'] = "Тут ви можете знайти стрічку всіх статей на сайті"
        context['category_tags'] = ""
        context['category_photo'] = "/static/images/banner/banner-4.jpg"
        return context

class ItPostView(PostView):  
    def get_queryset(self):
         return Post.objects.filter(category=Post.IT)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = "Інформаційні технології"
        context['category_description'] = "На цій сторінці зібрано найпопулярніші матеріали для підготовки до олімпіади з інформатики,а також опрацьовано матеріали з шкільного курсу інформатики."
        context['category_tags'] = ""
        context['category_photo'] = "/static/images/banner/programming.jpg"
        return context
         

class ProgrammingPostView(PostView):
    def get_queryset(self):
         return Post.objects.filter(category=Post.PROGRAMMING)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = "Програмування"
        context['category_description'] = "Збірка статей з шкільного курсу 5-11 класів з програмування."
        context['category_tags'] = ""
        context['category_photo'] = "/static/images/banner/banner-4.jpg"
        return context
         

class SchoolPostView(PostView):
    def get_queryset(self):
         return Post.objects.filter(category=Post.SCHOOL)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = "Шкільна інформатика"
        context['category_description'] = "На цій сторінці зібрано найпопулярніші матеріали для підготовки до олімпіади з інформатики,а також опрацьовано матеріали з шкільного курсу інформатики."
        context['category_tags'] = ""
        context['category_photo'] = "/static/images/banner/banner-5.jpg"
        return context
         
class ScratchPostView(PostView):
    def get_queryset(self):
         return Post.objects.filter(category=Post.SCRATCH)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = "Scratch"
        context['category_description'] = "Скретч — інтерпретована динамічна візуальна мова програмування основана і реалізована на Squeak. Завдяки динамічності, вона дає змогу змінювати код навіть під час виконання."
        context['category_tags'] = ""
        context['category_photo'] = "/static/images/banner/banner-5.jpg"
        return context
         