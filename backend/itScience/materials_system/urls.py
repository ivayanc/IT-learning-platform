from django.urls import path
from django.conf.urls import handler404
from django.views.generic.base import TemplateView

from . import views

handler404 = "materials_system.views.view_404"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', TemplateView.as_view(template_name='materials_system/about.html'), name='about'),
    path('it/', views.ItPostView.as_view(), name='it'),
    path('programming/', views.ProgrammingPostView.as_view(), name='programming'),
    path('school/', views.SchoolPostView.as_view(), name='school'),
    path('scratch/', views.ScratchPostView.as_view(), name='scratch'),
    path('news/', views.NewsPostView.as_view(), name='news'),
    
    path('sendComment/', views.sendComment, name="sendComment"),

    path('posts/', views.PostView.as_view(), name='posts'),
    path('poststag/<str:tag>', views.PostViewTag.as_view(), name='posts-tag'),
    path('posts/create/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:id>/', views.SinglePostView.as_view(), name='post-details'),
    path('posts/<int:id>/favorite_post', views.AddToFavoriteView.as_view(), name='post-favorite'),
    path('posts/<int:id>/update/', views.PostUpdateView.as_view(), name='post-update'),
    #path('posts/<int:id>/delete', views.PostDeleteView.as_view(), name='post-details'),

    path('hashtags/create/', views.HashTagCreateView.as_view(), name='hashtag-create'),
    path('hashtags/', views.HashTagListView.as_view(), name='hashtag-list'),
    path('hashtags/<int:id>/', views.HashTagUpdate.as_view(), name='hashtag-details'),

]