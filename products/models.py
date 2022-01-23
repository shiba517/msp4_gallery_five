from django.db import models
from django.contrib.auth.models import User
import random


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    screen_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_screen_name(self):
        return self.screen_name

    
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True, editable=False)
    name = models.CharField(max_length=80)
    artist_name = models.CharField(max_length=80)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=4, decimal_places=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    wishlisted = models.ManyToManyField('profiles.UserProfile', blank=True)


class Reviews(models.Model):
    class Meta:
        verbose_name_plural = 'Reviews'

    title = models.CharField(max_length=100)
    review = models.TextField(max_length=500)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.title
