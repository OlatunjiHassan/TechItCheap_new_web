from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages

# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            email_message = f"Through the Contact Us Page\nMessage from {name} ({email}):\n\n{message}"

            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.SUPPORT_TEAM_EMAIL],
                fail_silently=False,
            )

            messages.success(request, "You have contacted us successfully!")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contactus/contactus.html', {'form':form})