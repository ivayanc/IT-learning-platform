from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('about/', TemplateView.as_view(template_name='materials_system/about.html'), name='about'),
    path('it/', views.ItPostView.as_view(), name='it'),
    path('programming/', views.ProgrammingPostView.as_view(), name='programming'),
    path('school/', views.SchoolPostView.as_view(), name='school'),
    path('scratch/', views.ScratchPostView.as_view(), name='scratch'),
    path('posts/', views.PostView.as_view(), name='posts'),
    path('posts/<int:pk>', views.SinglePostView.as_view(), name='post-details'),
    path('posts/create', views.PostCreateView.as_view(), name='post-create'),
]