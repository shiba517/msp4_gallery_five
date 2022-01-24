from django import forms
from .models import Product, Category, Reviews


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('wishlisted',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        screen_names = [(c.id, c.get_screen_name()) for c in categories]

        self.fields['category'].choices = screen_names
        self.fields['price'].widget.attrs['min'] = 1
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = [
            'title', 'review',
        ]