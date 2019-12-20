from django.urls import path
from django.views.generic.base import TemplateView


from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='olympiad_system'),
    #path('<int:id>/', TemplateView.as_view(template_name='olympiad_system/olympiad.html'), name='olympiad'),
    path('<int:id>/', views.OlympiadView.as_view(), name='olympiad'),
    path('<int:pk>/<int:id>', TemplateView.as_view(template_name='olympiad_system/task.html'), name='task'),
    path('verify/', TemplateView.as_view(template_name='olympiad_system/verify.html'), name='task_verify'),
    path('<int:pk>/verify/', TemplateView.as_view(template_name='olympiad_system/verify_list.html'), name='verify_list'),
    #path('scratch/', views.ScratchPostView.as_view(), name='scratch'),
    #path('posts/', views.PostView.as_view(), name='posts'),
    #path('posts/<int:pk>', views.SinglePostView.as_view(), name='post-details'),
]