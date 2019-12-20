from django.shortcuts import render

from materials_system.models import Post
from .models import Olympiad

from django.views.generic import (
        TemplateView,
        ListView, 
        DetailView,
        CreateView, 
        UpdateView,
        DeleteView
)

# @login_required
class IndexView(TemplateView):
    template_name = 'olympiad_system/olympiad_system.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['registred_olympiads'] = Olympiad.objects.all().filter(participants__in=[self.request.user], is_ended=False).order_by('start_time')[:6]
        context['upcoming_olympiads'] = Olympiad.objects.filter(olymp_type=Olympiad.PUBLIC).exclude(participants__in=[self.request.user]).order_by('start_time')[:6]
        context['ended_olympiads'] = Olympiad.objects.filter(participants__in=[self.request.user], is_ended=True).order_by('start_time')[:6]
        return context


# class VerifySolutionView(DetailView):
#     template_name = 'olympiad_system/verify.html'
    
#     queryset = Post.objects.all()

#     def get_object(self, queryset=None):
#         id_ = self.kwargs.get("id")
#         post = get_object_or_404(Post, pk=id_)
#         post.views += 1
#         post.save()
#         return post
    
#     def get_context_data(self, **kwargs):
                
#         context = super().get_context_data(**kwargs)
#         context['latest_posts'] = Post.objects.all().filter(category=context['object'].category)[:3]
#         context['is_favorite'] = False
#         if len(self.get_object().favorite.filter(id = self.request.user.pk)):
#             context['is_favorite'] = True

#         return context