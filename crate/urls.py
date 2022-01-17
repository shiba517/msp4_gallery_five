from django.urls import path
from . import views

urlpatterns = [
    path('', views.crate, name='crate'),
    path('add/<item_id>/', views.add_to_crate, name='add_to_crate'),
    path('adjust/<item_id>/', views.adjust_crate, name='adjust_crate'),
    path('remove/<item_id>/', views.remove_from_crate, name='remove_from_crate'),
]