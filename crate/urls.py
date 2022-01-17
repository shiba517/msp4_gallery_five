from django.urls import path
from . import views

urlpatterns = [
    path('', views.crate, name='crate'),
    path('add/<item_id>/', views.add_to_crate, name='add_to_crate'),
]