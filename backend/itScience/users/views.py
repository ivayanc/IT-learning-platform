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
from .models import SystemUser
from .forms import SystemUserChangeForm, SystemUserCreationForm,SystemUserLoginForm



class SingUp(CreateView):
    form_class = SystemUserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'registration/singup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Реєстрація"
        context['button_text'] = "Зареєструватися"
        
        return context

class Login(FormView):
    form_class = SystemUserLoginForm
    template_name = 'registration/singup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Вхід"
        context['button_text'] = "Увійти"
        return context

    
class ProfileView(DetailView):
    template_name = 'registration/profile.html'
    
    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(SystemUser, pk=id_)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs) # get the default context data
        context['favorites'] = 1
        print(context)
        return context

class ProfileUpdateView(UpdateView):
    template_name = 'registration/edit.html'
    form_class = SystemUserChangeForm
    
    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(SystemUser, pk=id_)