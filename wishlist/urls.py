from django.urls import path
from . import views

urlpatterns = [
    # path('', views.wishlist, name='wishlist'),
    path('', views.wishlist, name='wishlist'),
    path('<int:product_id>/', views.add_wishlist, name='add_wishlist'),
]