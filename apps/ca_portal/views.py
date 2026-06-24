from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import RegisterForm
from .forms import Azeo_idForm
from .models import Extendeduser
from .models import Azeo_id_user
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import get_connection, EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError

def Registration(request):
    return render(request,'ca_portal/ca.html')

def user_register(request):
    template = 'ca_portal/register.html'  # Template for rendering the form

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = RegisterForm(request.POST)
        
        # Check whether it's valid
        if form.is_valid():
            # Check if the email already exists
            if Extendeduser.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            else:
                # Create an Extendeduser instance
                extendeduser = Extendeduser()
                extendeduser.first_name = form.cleaned_data['first_name']
                extendeduser.last_name = form.cleaned_data['last_name']
                extendeduser.phone_number = form.cleaned_data['phone_number']
                extendeduser.alternate_phone_number = form.cleaned_data['alternate_phone_number']
                extendeduser.college = form.cleaned_data['college']
                extendeduser.current_year = form.cleaned_data['current_year']
                extendeduser.permanent_address = form.cleaned_data['permanent_address']
                extendeduser.state = form.cleaned_data['state']
                extendeduser.email = form.cleaned_data['email']
                extendeduser.pincode = form.cleaned_data['pincode']

                # Save the user data
                extendeduser.save()

                # Prepare the email
                subject = "Successfully registered for AZeotropy Campus Ambassador"
                name1 = str(extendeduser.first_name).title()
                html_message = render_to_string("ca_portal/mail.html", {'name': name1})
                message = strip_tags(html_message)
                to_email = extendeduser.email

                connection = get_connection()
                connection.open()
                email = EmailMultiAlternatives(subject, message, 'no-reply-registration@azeotropy.org', [to_email])
                email.attach_alternative(html_message, 'text/html')
                email.send()
                connection.close()

                # email = EmailMultiAlternatives("Urgently 2 packets of sutta required", "Dear OC, As a former web manager me Daddy Jones, with emotional support from Diddy hereby request you to urgently send two packets of sutta to room 209 along with your female design manager.", 'suttarequired@azeotropy.org', ["22b0389@iitb.ac.in"])

                # Success message
                success_message = 'You have successfully registered on CA portal'
                return render(request, "ca_portal/ca.html", {'message': success_message})
    
    # If not a POST request, display the empty form
    else:
        form = RegisterForm()
    
    return render(request, template, {'form': form})

def AZeo_id(request):
    # if this is a POST request we need to process the form data
        template = 'main_website/register_user.html'

        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = Azeo_idForm(request.POST)
            # check whether it's valid:
            if form.is_valid():

                if Azeo_id_user.objects.filter(email=form.cleaned_data['email']).exists():
                    return render(request, template, {
                        'form': form,
                        'error_message': 'Email already exists.'
                    })



                else:
                    # print('hellow world')
                    # Create the user:

                    # user = User.objects.create_user(
                    #     # form.cleaned_data['username'],
                    #     form.cleaned_data['email']

                    # )

                    extendeduser = Azeo_id_user()
                    extendeduser.first_name = form.cleaned_data['first_name']
                    extendeduser.last_name = form.cleaned_data['last_name']
                    extendeduser.phone_number = form.cleaned_data['phone_number']
                    extendeduser.alternate_phone_number = form.cleaned_data['alternate_phone_number']
                    extendeduser.college = form.cleaned_data['college']
                    extendeduser.current_year = form.cleaned_data['current_year']
                    extendeduser.permanent_address = form.cleaned_data['permanent_address']
                    extendeduser.state = form.cleaned_data['state']
                    extendeduser.email = form.cleaned_data['email']
                    extendeduser.pincode = form.cleaned_data['pincode']
                    Azeo_no =f"AZ-{extendeduser.first_name[:3].upper()}-{Azeo_id_user.objects.only('id').last().id+1}"
                    extendeduser.azeo_id = Azeo_no
                    # extendeduser.user = user
                    extendeduser.save()





                    subject = "Successfully created your AZeo ID "
                    # message = f'congratulations {extendeduser.first_name}{extendeduser.last_name} have successfully registered on CA portal'
                    to_email = extendeduser.email

                    name1 = str(extendeduser.first_name).title()
                    collegename = str(extendeduser.college).title()
                    html_message = render_to_string("main_website/email.html",{'name':name1,'college':collegename,'AZeo_ID':Azeo_no})
                    message = strip_tags(html_message)

                    email3 = EmailMultiAlternatives(subject,
                                message,
                                'seemon@azeotropy.org',
                                [to_email],
                                )
                    email3.attach_alternative(html_message,'text/html')

                            # Generate PDF
                    # pdf_buffer = generate_pdf({
                    #     'first_name': extendeduser.first_name,
                    #     'last_name': extendeduser.last_name,
                    #     'azeo_id': Azeo_no
                    # })
                      # Attach PDF to the email
                    # email3.attach('Visiting_Pass_Card.pdf', pdf_buffer.getvalue(), 'application/pdf')

                    email3.send()

                    # send_mail(
                    #             subject,
                    #             message,
                    #             from_email,
                    #             [to_email],
                    #             fail_silently=False,
                    #         )
                    # extendeduser.save()
                    message = 'You have successfully registered on CA portal'
                    return render(request, "main_website/confirmation_page.html",{'AZeo_ID':Azeo_no})




                    # redirect to home page:
                    #return redirect('registration_ca:index')

    # No post data availabe, let's just show the page.
        else:
            form = Azeo_idForm()

        return render(request, template, {'form': form})