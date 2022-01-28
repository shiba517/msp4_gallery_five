from django.urls import path
from . import views

urlpatterns = [
    path('error404', views.error404, name='error404'),
    path('error500', views.error500, name='error500'),
]