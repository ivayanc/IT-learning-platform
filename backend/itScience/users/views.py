from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.http import HttpResponse, StreamingHttpResponse, FileResponse, Http404
from django.views.generic import (
        TemplateView,
        ListView, 
        DetailView,
        CreateView, 
        UpdateView,
        DeleteView,
        FormView
)
from materials_system.models import Post
from .models import SystemUser
from .forms import SystemUserChangeForm, SystemUserCreationForm, SystemUserLoginForm


class SingUp(CreateView):
    form_class = SystemUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/singup.html'


class ProfileView(DetailView):
    template_name = 'registration/profile.html'
    
    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(SystemUser, pk=id_)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs) # get the default context data
        context['favorites'] = Post.objects.filter(favorite__in=[self.get_object().pk])
        context['posts'] = Post.objects.filter(moderator__in=[self.get_object().pk])
        return context

class ProfileUpdateView(UpdateView):
    template_name = 'registration/edit.html'
    form_class = SystemUserChangeForm
    
    def form_valid(self, form):
        response = super().form_valid(form)
        new_password = self.request.POST.get("password2")
        if(new_password != ""):
            user = SystemUser.objects.get(pk=self.request.POST.get("user"))
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(self.request, user) 
        return response

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        if(str(self.request.user) == "AnonymousUser"):
            raise Http404("no permision")
        if(self.request.user.role.can_edit_users == False and str(self.request.user) != str(get_object_or_404(SystemUser, pk=id_).username)):
            raise Http404("no permision")
        return get_object_or_404(SystemUser, pk=id_)