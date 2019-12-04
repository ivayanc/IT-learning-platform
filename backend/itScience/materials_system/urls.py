from django.urls import path
from django.views.generic.base import TemplateView


from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('it/', views.PostsView.as_view(), name='it'),
    path('programming/', views.PostsView.as_view(), name='programming'),
    path('school/', views.PostsView.as_view(), name='school'),
]