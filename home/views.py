from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string
from django.conf import settings

from .models import ContactUs
from .forms import ContactUsForm


def index(request):
    form = ContactUsForm()

    if request.method == 'POST':
        form = ContactUsForm(request.POST, request.FILES)

        message_name = render_to_string(
            'home/contact_us_emails/email_to_recieve_subject.txt',
            {'name': request.POST['name']})
        print(message_name)
        # message_message = request.POST['message']
        message_message = render_to_string(
            'home/contact_us_emails/email_to_recieve_body.txt',
            {'message': request.POST['message']})
        message_email = request.POST['email']

        send_mail(
            message_name,  # subject of the email
            message_message,  # message of the email
            message_email,  # email recieved from..
            [settings.DEFAULT_FROM_EMAIL],  # email recieved to..
        )
        print('EMAIL SHOULD BE SENT')

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, f'We have recieved\
                your message will get back to you with 48 hours.')
            return redirect(reverse('home'))

    context = {
        'form': form,
    }
    # Returns user to home/index page
    return render(request, 'home/index.html', context)