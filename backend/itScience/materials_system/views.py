from django.shortcuts import render, get_object_or_404, redirect, render_to_response 
from django.http import HttpResponse, StreamingHttpResponse, FileResponse, Http404
from django.views.generic import (
        TemplateView,
        ListView, 
        DetailView,
        CreateView, 
        UpdateView,
        DeleteView
)
from .models import Post, PostHashTag, HashTag, Comments
from olympiad_system.models import Olympiad
from users.models import SystemUser
from .forms import PostCreateForm, HashTagForm, CommentsForm
from django.shortcuts import render, redirect
import simplejson as json
from django.utils import timezone, dateformat
import pytz
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
        return post
    
    def get_context_data(self, **kwargs):
        id_ = self.kwargs.get("id")
        post = get_object_or_404(Post, pk=id_)
        post.views = post.views + 1
        post.save()
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.all()[:3]
        context['is_favorite'] = False
        context['comments'] = Comments.objects.all().filter(post = self.kwargs.get("id")).order_by('-date')
        #print(context['comments'][0].text)
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
        return context

class HashTagListView(TemplateView):
    template_name = 'materials_system/hashtag_list.html'

    def get_context_data(self, **kwargs):
        if(str(self.request.user) == "AnonymousUser"):
            raise Http404("no permision")
        if(self.request.user.role.can_change_hashtags == False):
            raise Http404("no permision")
        context = super().get_context_data(**kwargs)
        context['all_hashtags'] = HashTag.objects.all()  
        return context

class HashTagCreateView(CreateView):
    template_name = 'materials_system/hashtag_create.html'
    form_class = HashTagForm
    queryset = HashTag.objects.all()

    def form_valid(self, form):
        response = super().form_valid(form)
        hashtag_parent = self.request.POST.get("hashtag_parent")
        if(hashtag_parent == ""):
            return response
        hashtag = self.request.POST.get("tag_name")
        tagparent = HashTag.objects.get(tag_name=hashtag_parent)
        tag = HashTag.objects.get(tag_name=hashtag)
        tag.tag_parent = tagparent
        tag.save()
        return response

    def get_context_data(self, **kwargs):
        if(str(self.request.user) == "AnonymousUser"):
            raise Http404("no permision")
        if(self.request.user.role.can_change_hashtags == False):
            raise Http404("no permision")
        context = super().get_context_data(**kwargs)
        context['all_hashtags'] = HashTag.objects.all()
        hashtags = HashTag.objects.all()
        context['hashtagsArray'] = []
        context['buttonName'] = 'Додати'
        for hashtag in hashtags:
            context['hashtagsArray'].append(hashtag.tag_name)
        context['hashtagsArray'] = json.dumps(context['hashtagsArray'])
        return context

class SinglePostView(DetailView):
    template_name = 'materials_system/post_page.html'
    
    queryset = Post.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        post = get_object_or_404(Post, pk=id_)
        return post
    
    def get_context_data(self, **kwargs):
        month = ['січня', 'лютого', 'березеня', 'квітня', 'травня', 'червня', 'липня', 'серпня', 'вересня', 'жовтня', 'листопада', 'грудня']
        id_ = self.kwargs.get("id")
        post = get_object_or_404(Post, pk=id_)
        post.views = post.views + 1
        post.save()
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.all()[:3]
        context['is_favorite'] = False
        context['comments'] = Comments.objects.all().filter(post = self.kwargs.get("id")).order_by('-date')
        for comment in context['comments']:
            comment.date1 = str(dateformat.format(comment.date, 'd')) + " " + str(month[int(dateformat.format(comment.date, 'm')) - 1]) + " " + str(dateformat.format(comment.date, 'Y')) + " року"
        
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
        return context

class HashTagListView(TemplateView):
    template_name = 'materials_system/hashtag_list.html'

    def get_context_data(self, **kwargs):
        if(str(self.request.user) == "AnonymousUser"):
            raise Http404("no permision")
        if(self.request.user.role.can_change_hashtags == False):
            raise Http404("no permision")
        context = super().get_context_data(**kwargs)
        context['all_hashtags'] = HashTag.objects.all()  
        return context

def sendComment(request):
    if request.method == 'POST':
        post, user = request.POST.get("postId").split(", ")
        post = Post.objects.get(pk = post)
        user = SystemUser.objects.get(pk = user)
        text = request.POST.get("comment")
        Comments.objects.create(post = post, user = user, text = text, date=timezone.now())
    return redirect('post-details', id=request.POST.get("postId").split(", ")[0])

class HashTagUpdate(UpdateView):
    template_name = 'materials_system/hashtag_create.html'
    form_class = HashTagForm

    def form_valid(self, form):
        response = super().form_valid(form)
        hashtag_parent = self.request.POST.get("hashtag_parent")
        if(hashtag_parent == ""):
            return response
        hashtag = self.request.POST.get("tag_name")
        tagparent = HashTag.objects.get(tag_name=hashtag_parent)
        tag = HashTag.objects.get(tag_name=hashtag)
        tag.tag_parent = tagparent
        tag.save()
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hashtag_parent'] = ''
        try:
            context['hashtag_parent'] = HashTag.objects.get(id=self.kwargs.get("id")).tag_parent
        except:
            pass 
        context['all_hashtags'] = HashTag.objects.all()
        context['buttonName'] = 'Зберегти'
        hashtags = HashTag.objects.all()
        context['hashtagsArray'] = []
        for hashtag in hashtags:
            context['hashtagsArray'].append(hashtag.tag_name)
        context['hashtagsArray'] = json.dumps(context['hashtagsArray'])
        return context

    def get_object(self, queryset=None):
        if(str(self.request.user) == "AnonymousUser"):
            raise Http404("no permision")
        if(self.request.user.role.can_change_hashtags == False):
            raise Http404("no permision")
        id_ = self.kwargs.get("id")
        return  get_object_or_404(HashTag, pk=id_)
    

class PostCreateView(CreateView):
    template_name = 'materials_system/post_create.html'
    form_class = PostCreateForm
    queryset = Post.objects.all()
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.title = self.request.POST.get("title")
        post = Post.objects.get(title=self.object.title)
        try:
            self.object.hashtags = json.loads(self.request.POST.get("hashtagsAdd"))
            for hashtag in self.object.hashtags:
                hashTagM = HashTag.objects.get(tag_name=hashtag)
                PostHashTag.objects.create(post=post, tag=hashTagM)
        except:
            print("error with adding hashtags to post")
        try:
            self.object.hashtagsDelete = json.loads(self.request.POST.get("hashtagsDelete"))
            for hashtag in self.object.hashtagsDelete:
                hashTagM = HashTag.objects.get(tag_name=hashtag)
                PostHashTag.objects.get(post=post, tag=hashTagM).delete()
        except:
            print("error with deleting hashtags from post")
        post.published = timezone.now()
        post.save()
        return response

    def get_context_data(self, **kwargs):
        if(str(self.request.user) == "AnonymousUser"):
            raise Http404("no permision")
        if(self.request.user.role.can_post == False):
            raise Http404("no permision")
        context = super().get_context_data(**kwargs)
        hashtags = HashTag.objects.all()
        context['all_hashtags'] = HashTag.objects.all()
        context['hashtagsArray'] = []
        for hashtag in hashtags:
            context['hashtagsArray'].append(hashtag.tag_name)
        context['hashtagsArray'] = json.dumps(context['hashtagsArray'])
        return context

class PostUpdateView(UpdateView):
    template_name = 'materials_system/post_create.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.title = self.request.POST.get("title")
        post = Post.objects.get(title=self.object.title)
        try:
            self.object.hashtags = json.loads(self.request.POST.get("hashtagsAdd"))
            for hashtag in self.object.hashtags:
                hashTagM = HashTag.objects.get(tag_name=hashtag)
                PostHashTag.objects.create(post=post, tag=hashTagM)
        except:
            print("error with adding hashtags to post")
        try:
            self.object.hashtagsDelete = json.loads(self.request.POST.get("hashtagsDelete"))
            for hashtag in self.object.hashtagsDelete:
                hashTagM = HashTag.objects.get(tag_name=hashtag)
                PostHashTag.objects.get(post=post, tag=hashTagM).delete()
        except:
            print("error with deleting hashtags from post")
        return super().form_valid(form)

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        if(str(self.request.user) == "AnonymousUser"):
            raise Http404("no permision")
        if(self.request.user.role.can_post == True and get_object_or_404(Post, pk=id_).moderator == self.request.user or self.request.user.role.can_edit_posts == True):
            return  get_object_or_404(Post, pk=id_)
        else:
            raise Http404("no permision")
    
    def get_context_data(self, **kwargs):
        id_ = self.kwargs.get("id")
        post = Post.objects.get(id=id_)
        context = super().get_context_data(**kwargs)
        hashtags = HashTag.objects.all()
        context['hashtagsArray'] = []
        for hashtag in hashtags:
            context['hashtagsArray'].append(hashtag.tag_name)
        hashtags = HashTag.objects.all()
        context['all_hashtags'] = HashTag.objects.all()
        context['hashtagsArray'] = json.dumps(context['hashtagsArray'])
        context['hashtagsArray'] = json.dumps(context['hashtagsArray'])
        context['addedHashtags'] = []
        hashtagsPost = PostHashTag.objects.all().filter(post = post)
        for hashtagPost in hashtagsPost:
            context['addedHashtags'].append(hashtagPost.tag.tag_name) 
        return context

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
        hashtags = set()
        hashtags.add(HashTag.objects.get(tag_name=self.kwargs.get("tag")))
        hash_tags = HashTag.objects.filter(tag_parent=HashTag.objects.get(tag_name=self.kwargs.get("tag")))
        for hash_tag in hash_tags:
            hashtags.add(hash_tag)
            phash_tags = HashTag.objects.filter(tag_parent=hash_tag)
            while(len(phash_tags) > 0):
                for phash_tag in phash_tags:
                    hashtags.add(phash_tag)
                phash_tags = HashTag.objects.filter(tag_parent=phash_tags)
        posts = set()
        for hashtag in hashtags:
            query = PostHashTag.objects.filter(tag__tag_name=hashtag.tag_name)

            for post in query:
                posts.add(post.post.id)
        return Post.objects.filter(id__in = posts).order_by('-published')

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
         
