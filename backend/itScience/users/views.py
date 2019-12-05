from django.shortcuts import render
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