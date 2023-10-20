# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_post_list, name='blog_post_list'),
    path('<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    path('comment/<int:pk>/', views.comment_view, name='comment_view'), 
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('new/', views.blog_post_new, name='blog_post_new'),
    path('<int:pk>/edit/', views.blog_post_edit, name='blog_post_edit'),
    path('<int:pk>/delete/', views.blog_post_delete, name='blog_post_delete'),
    path('<int:pk>/approve/', views.blog_post_approve, name='blog_post_approve'),

]

