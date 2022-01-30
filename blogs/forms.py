from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title', 'article', 'image',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['maxlength'] = 80

class PublishBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'publish',
        ]
