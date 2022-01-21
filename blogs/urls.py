from django.urls import path
from django import forms

from . import views, models

urlpatterns = [
    path('', views.view_blogs, name='view_blogs'),
    path('read_blog/<int:blog_id>', views.read_blog, name='read_blog'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('reject_blog/<int:blog_id>', views.reject_blog, name='reject_blog'),
]