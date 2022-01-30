from django import forms

from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = [
            'name', 'message', 'email',
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        
        self.fields['email'].widget.attrs['type'] = 'email'
        self.fields['name'].widget.attrs['maxlength'] = 10