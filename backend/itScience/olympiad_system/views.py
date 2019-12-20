from django.shortcuts import render, get_object_or_404, redirect

from materials_system.models import Post
from .models import Olympiad, Task

from django.views.generic import (
        TemplateView,
        ListView, 
        DetailView,
        CreateView, 
        UpdateView,
        DeleteView
)

from datetime import datetime
from django.utils import timezone


class IndexView(TemplateView):
    template_name = 'olympiad_system/olympiad_system.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['upcoming_olympiads'] = Olympiad.objects.filter(olymp_type=Olympiad.PUBLIC).exclude(participants__in=[self.request.user], is_ended=False).order_by('start_time')[:6]
            context['registred_olympiads'] = Olympiad.objects.all().filter(participants__in=[self.request.user], is_ended=False).order_by('start_time')[:6]
            context['ended_olympiads'] = Olympiad.objects.filter(participants__in=[self.request.user], is_ended=True).order_by('start_time')[:6]
        else:
            context['upcoming_olympiads'] = Olympiad.objects.filter(olymp_type=Olympiad.PUBLIC, is_ended=False).order_by('start_time')[:6]

        return context

class OlympiadView(DetailView):
    template_name = 'olympiad_system/olympiad.html'
    
    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Olympiad, pk=id_)

    def get_context_data(self, **kwargs):
        context = super(OlympiadView, self).get_context_data(**kwargs) # get the default context data
        
        olymp = self.get_object()
        end_time = olymp.start_time + olymp.duration
        now = timezone.now()

        context['is_time_started'] = False
        context['is_time_ended'] = False

        if  now > end_time:
            context['is_time_started'] = True
            context['is_time_ended'] = True
        elif now > olymp.start_time:
            context['is_time_started'] = True

        o = olymp.participants
        print(o)
        
        context['not_registred'] = not olymp.participants.filter(id=self.request.user.id).exists()
        context['tasks'] = Task.objects.filter(olympiad=olymp)
        return context

class OlympiadRegisterView(UpdateView):

    http_method_names = ['post', ]
    model = Olympiad

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return  get_object_or_404(Olympiad, pk=id_)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.participants.filter(id=request.user.id).exists():
            self.object.participants.remove(request.user)
        else:
            self.object.participants.add(request.user)

        return redirect('olympiad', id=self.object.pk)


class TaskSendSolutionView(UpdateView):

    http_method_names = ['post', ]
    model = Olympiad

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return  get_object_or_404(Olympiad, pk=id_)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.participants.filter(id=request.user.id).exists():
            self.object.participants.remove(request.user)
        else:
            self.object.participants.add(request.user)

        return redirect('olympiad', id=self.object.pk)

class TaskView(DetailView):
    template_name = 'olympiad_system/task.html'
    
    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        task_id_ = self.kwargs.get("task_id")
        task = get_object_or_404(Task, olympiad=id_, task_alias=task_id_)

        return task


    def get_context_data(self, **kwargs):
        context = super(TaskView, self).get_context_data(**kwargs) # get the default context data
        
        task = self.get_object()
        
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