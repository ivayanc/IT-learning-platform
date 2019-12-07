from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import SystemUser


from .forms import SystemUserCreationForm

class SignUpView(CreateView):
    form_class = SystemUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/singup.html'

class ProfileView(DetailView):
    template_name = 'registration/profile.html'
    queryset = SystemUser.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs) # get the default context data
        context['favorites'] = 1
        print(context)
        return context
