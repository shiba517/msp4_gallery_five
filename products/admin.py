from django.contrib import admin
from .models import Product, Category, Reviews


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'artist_name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'screen_name',
        'name',
    )

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'review',
        'auther',
        'product',
        'date',
        'publish',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reviews, ReviewAdmin)
