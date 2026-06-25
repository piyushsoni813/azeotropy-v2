import logging

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .forms import RegisterForm, Azeo_idForm
from .models import Extendeduser, Azeo_id_user

logger = logging.getLogger(__name__)


def Registration(request):
    return render(request, 'ca_portal/ca.html')


def user_register(request):
    template = 'ca_portal/register.html'

    if request.method != 'POST':
        return render(request, template, {'form': RegisterForm()})

    form = RegisterForm(request.POST)

    if not form.is_valid():
        return render(request, template, {'form': form})

    email = form.cleaned_data['email']

    # Guard against duplicate emails — the unique constraint on the model is
    # the real enforcement, but checking here gives a friendlier message.
    if Extendeduser.objects.filter(email=email).exists():
        return render(request, template, {
            'form': form,
            'error_message': 'This email is already registered as a Campus Ambassador.',
        })

    try:
        ca = Extendeduser.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            phone_number=form.cleaned_data['phone_number'],
            alternate_phone_number=form.cleaned_data.get('alternate_phone_number', ''),
            college=form.cleaned_data['college'],
            current_year=form.cleaned_data['current_year'],
            permanent_address=form.cleaned_data['permanent_address'],
            state=form.cleaned_data['state'],
            email=email,
            pincode=form.cleaned_data.get('pincode', ''),
        )
    except IntegrityError:
        # Concurrent submission slipped past the exists() check above.
        return render(request, template, {
            'form': form,
            'error_message': 'This email is already registered. Please check your inbox for the confirmation email.',
        })

    # Registration is saved. Send confirmation email — but a mail failure
    # must NOT undo a successful registration, so we handle it gracefully.
    _send_confirmation(ca)

    return render(request, 'ca_portal/ca.html', {
        'success_message': f"Welcome aboard, {ca.first_name}! You've been registered as a Campus Ambassador. Check your inbox for a confirmation email.",
    })


def _send_confirmation(ca):
    """Send the CA welcome email. Logs on failure; does not raise."""
    try:
        name = ca.first_name.title()
        html_body = render_to_string('ca_portal/mail.html', {'name': name})
        text_body = strip_tags(html_body)

        msg = EmailMultiAlternatives(
            subject='Welcome to AZeotropy — Campus Ambassador Registration Confirmed',
            body=text_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[ca.email],
        )
        msg.attach_alternative(html_body, 'text/html')
        msg.send()
    except Exception:
        # Don't crash the request — the person is registered.
        # Log so the team can follow up manually if needed.
        logger.exception(
            "Confirmation email failed for CA registration id=%s email=%s",
            ca.pk, ca.email,
        )


def AZeo_id(request):
    template = 'main_website/register_user.html'

    if request.method != 'POST':
        return render(request, template, {'form': Azeo_idForm()})

    form = Azeo_idForm(request.POST)

    if not form.is_valid():
        return render(request, template, {'form': form})

    if Azeo_id_user.objects.filter(email=form.cleaned_data['email']).exists():
        return render(request, template, {
            'form': form,
            'error_message': 'Email already exists.',
        })

    extendeduser = Azeo_id_user(
        first_name=form.cleaned_data['first_name'],
        last_name=form.cleaned_data['last_name'],
        phone_number=form.cleaned_data['phone_number'],
        alternate_phone_number=form.cleaned_data.get('alternate_phone_number', ''),
        college=form.cleaned_data['college'],
        current_year=form.cleaned_data['current_year'],
        permanent_address=form.cleaned_data['permanent_address'],
        state=form.cleaned_data['state'],
        email=form.cleaned_data['email'],
        pincode=form.cleaned_data.get('pincode'),
    )

    # Safe ID generation: use the DB-assigned pk after save instead of
    # reading last().id (which crashes on empty table and has race conditions).
    extendeduser.save()
    Azeo_no = f"AZ-{extendeduser.first_name[:3].upper()}-{extendeduser.pk}"
    extendeduser.azeo_id = Azeo_no
    extendeduser.save(update_fields=['azeo_id'])

    try:
        name = extendeduser.first_name.title()
        college = extendeduser.college.title()
        html_body = render_to_string('main_website/email.html', {
            'name': name,
            'college': college,
            'AZeo_ID': Azeo_no,
        })
        msg = EmailMultiAlternatives(
            subject='Your AZeo ID — AZeotropy',
            body=strip_tags(html_body),
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[extendeduser.email],
        )
        msg.attach_alternative(html_body, 'text/html')
        msg.send()
    except Exception:
        logger.exception(
            "AZeo ID email failed for id=%s email=%s",
            extendeduser.pk, extendeduser.email,
        )

    return render(request, 'main_website/confirmation_page.html', {'AZeo_ID': Azeo_no})