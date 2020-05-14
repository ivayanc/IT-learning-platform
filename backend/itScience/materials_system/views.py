from django.shortcuts import render, get_object_or_404
from django.views.generic import (
        TemplateView,
        ListView, 
        DetailView,
        CreateView, 
        UpdateView,
        DeleteView
)
from .models import Post, PostHashTag, HashTag
from olympiad_system.models import Olympiad
from .forms import PostCreateForm
from django.shortcuts import render, redirect

class IndexView(TemplateView):
    template_name = 'materials_system/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.all().order_by('-published')[:6]
        #context['latest_news'] = Post.objects.all().filter(category=Post.OTHER).order_by('-published')[:3]
        context['olympiads'] = Olympiad.objects.all().filter(olymp_type=Olympiad.PUBLIC,is_ended=False).order_by('start_time')[:3]
        
        return context

class SinglePostView(DetailView):
    template_name = 'materials_system/post_page.html'
    
    queryset = Post.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        post = get_object_or_404(Post, pk=id_)
        post.views += 1
        post.save()
        return post
    
    def get_context_data(self, **kwargs):
                
        context = super().get_context_data(**kwargs)
        #context['latest_posts'] = Post.objects.all().filter(category=context['object'].category)[:3]
        context['is_favorite'] = False
        if len(self.get_object().favorite.filter(id = self.request.user.pk)):
            context['is_favorite'] = True

        context['hash_tags'] = set()
        hash_tags = PostHashTag.objects.all().filter(post = self.kwargs.get("id"))
        for hash_tag in hash_tags:
            parent = hash_tag.tag.tag_parent
            while(parent != None):
                context['hash_tags'].add(parent)
                parent = parent.tag_parent
            context['hash_tags'].add(hash_tag.tag)
        print(context['hash_tags'])
        return context
    
class PostCreateView(CreateView):
    template_name = 'materials_system/post_create.html'
    form_class = PostCreateForm
    queryset = Post.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    template_name = 'materials_system/post_create.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return  get_object_or_404(Post, pk=id_)

class AddToFavoriteView(UpdateView):

    http_method_names = ['post', ]
    model = Post

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return  get_object_or_404(Post, pk=id_)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.favorite.filter(id=request.user.id).exists():
            self.object.favorite.remove(request.user)
        else:
            self.object.favorite.add(request.user)

        return redirect('post-details', id=self.object.pk)
  
class PostView(ListView):
    def get_queryset(self):
         return Post.objects.order_by('-published')

    model = Post
    paginate_by = 9
    context_object_name = 'posts'
    template_name = 'materials_system/posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = "Статті"
        context['category_description'] = "Тут ви можете знайти стрічку всіх статей на сайті"
        context['category_tags'] = []
        context['category_photo'] = "/static/images/banner/banner-4.jpg"
        context['category_link'] = "/posts/"
        hash_tags = HashTag.objects.all().filter(tag_main=True)
        for hash_tag in hash_tags:
            context['category_tags'].append(hash_tag)
        return context

class PostViewTag(ListView):
    def get_queryset(self):
        query = PostHashTag.objects.filter(tag__tag_name=self.kwargs.get("tag"))
        posts = []
        for post in query:
            posts.append(post.post.id)
        print(posts)
        return Post.objects.filter(id__in = posts)

    model = Post
    paginate_by = 9
    context_object_name = 'posts'
    template_name = 'materials_system/postsTag.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = self.kwargs.get("tag")
        context['category_description'] = ""
        context['category_tags'] = []
        context['category_photo'] = "/static/images/banner/banner-4.jpg"
        context['category_link'] = "/poststag/" + self.kwargs.get("tag")
        hash_tags = HashTag.objects.all().filter(tag_parent__tag_name=self.kwargs.get("tag"))
        for hash_tag in hash_tags:
            context['category_tags'].append(hash_tag)
        return context

class ItPostView(PostView):  
    def get_queryset(self):
         return Post.objects.filter(category=Post.IT).order_by('-published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = "Інформаційні технології"
        context['category_description'] = "На цій сторінці зібрано найпопулярніші матеріали для підготовки до олімпіади з інформатики,а також опрацьовано матеріали з шкільного курсу інформатики."
        context['category_tags'] = ""
        context['category_photo'] = "/static/images/banner/programming.jpg"
        context['category_link'] = "/it/"
        return context
         
class ProgrammingPostView(PostView):
    def get_queryset(self):
         return Post.objects.filter(category=Post.PROGRAMMING).order_by('-published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = "Програмування"
        context['category_description'] = "Збірка статей з шкільного курсу 5-11 класів з програмування."
        context['category_tags'] = ""
        context['category_photo'] = "/static/images/banner/banner-4.jpg"
        context['category_link'] = "/programming/"
        return context
         
class SchoolPostView(PostView):
    def get_queryset(self):
         return Post.objects.filter(category=Post.SCHOOL).order_by('-published')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = "Шкільна інформатика"
        context['category_description'] = "На цій сторінці зібрано найпопулярніші матеріали для підготовки до олімпіади з інформатики,а також опрацьовано матеріали з шкільного курсу інформатики."
        context['category_tags'] = ""
        context['category_photo'] = "/static/images/banner/banner-5.jpg"
        context['category_link'] = "/school/"
        return context
         
class ScratchPostView(PostView):
    def get_queryset(self):
         return Post.objects.filter(category=Post.SCRATCH).order_by('-published')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = "Scratch"
        context['category_description'] = "Скретч — інтерпретована динамічна візуальна мова програмування основана і реалізована на Squeak. Завдяки динамічності, вона дає змогу змінювати код навіть під час виконання."
        context['category_tags'] = ""
        context['category_photo'] = "/static/images/banner/banner-5.jpg"
        context['category_link'] = "/scratch/"
        return context
         
class NewsPostView(PostView):
    def get_queryset(self):
         return Post.objects.filter(category=Post.OTHER).order_by('-published')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = "Новини"
        context['category_description'] = "Новини"
        context['category_tags'] = ""
        context['category_photo'] = "/static/images/banner/banner-5.jpg"
        context['category_link'] = "/news/"
        return context
         
