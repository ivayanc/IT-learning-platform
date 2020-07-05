from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
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
        print(context)
        return context

class ProfileUpdateView(UpdateView):
    template_name = 'registration/edit.html'
    form_class = SystemUserChangeForm
    
    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(SystemUser, pk=id_)