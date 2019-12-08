from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<int:id>', views.ProfileView.as_view(), name='profile'),
    path('<int:id>/edit/', views.ProfileUpdateView.as_view(), name='profile-edit'),
]