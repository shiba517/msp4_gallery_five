from django.urls import path
from django import forms

from . import views, models

urlpatterns = [
    path('', views.view_blogs, name='view_blogs'),
    # path('create_blog/', views.create_blog, name='create_blog'),
    # path('publish_blog/<int:blog_id>/', views.publish_blog, name='publish_blog'),
    path('read_blog/<int:blog_id>', views.read_blog, name='read_blog')
]