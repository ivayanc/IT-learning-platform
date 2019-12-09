from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.ProfileView.as_view(), name='profile'),
    path('singup/', views.SingUp.as_view(), name='singup'),
    path('login/', views.Login.as_view(), name='login'),
    path('<int:id>/edit/', views.ProfileUpdateView.as_view(), name='profile-edit'),
]