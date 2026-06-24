from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db import IntegrityError
from .forms import RegistrationForm
from .models import Registration
from .utils import generate_azeoid  # Assuming AZEOID generation function is in utils.py

def register(request):
    success_message = ""
    error_message = ""

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Check if user is already registered
            if Registration.objects.filter(email=email).exists():
                error_message = "You have already registered with this email!"
            else:
                name = form.cleaned_data['name']
                phone_number = form.cleaned_data['phone_number']
                year_of_study = form.cleaned_data['year_of_study']
                college_name = form.cleaned_data['college_name']
                azeoid = generate_azeoid(name, email)

                try:
                    # Save to Database
                    Registration.objects.create(
                        name=name, email=email, phone_number=phone_number, 
                        year_of_study=year_of_study, college_name=college_name, azeoid=azeoid
                    )

                    # Render Email Template
                    html_content = render_to_string("azeoid/mail.html", {
                        "name": name, "azeoid": azeoid
                    })
                    text_content = strip_tags(html_content)

                    # Email Setup
                    subject = "AZEOID Registration Successful!"
                    from_email = "your-email@example.com"  # Replace with actual sender email
                    recipient_list = [email]

                    email_message = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
                    email_message.attach_alternative(html_content, "text/html")
                    email_message.send()

                    success_message = "Registration successful! Check your email for your AZEOID."

                except IntegrityError:
                    error_message = "Something went wrong! Please try again."

    else:
        form = RegistrationForm()

    return render(request, 'azeoid/register.html', {
        'form': form,
        'success_message': success_message,
        'error_message': error_message
    })
