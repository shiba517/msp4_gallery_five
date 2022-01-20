from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'auther',
        'article',
        'date',
        'image',
        'publish',
    )

admin.site.register(Blog, BlogAdmin)
