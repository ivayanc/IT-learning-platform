from django.urls import path
from django.views.generic.base import TemplateView


from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='olympiad_system'),
    path('<int:id>/', views.OlympiadView.as_view(), name='olympiad'),
    path('<int:id>/register', views.OlympiadRegisterView.as_view(), name='olympiad_register'),
    path('<int:id>/<str:task_id>', views.TaskView.as_view(), name='olympiad_task'),

    path('verify/', TemplateView.as_view(template_name='olympiad_system/verify.html'), name='task_verify'),
    path('<int:pk>/verify/', TemplateView.as_view(template_name='olympiad_system/verify_list.html'), name='verify_list'),
]