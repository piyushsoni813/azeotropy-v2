from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import RegisterForm2
#from django.contrib import messages
from .models import User_Chem_e_cross
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def user_register2(request):
    # if this is a POST request we need to process the form data
    template = 'chem-e-cross/registration_page.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm2(request.POST)
        # check whether it's valid:
        if form.is_valid():

            if User_Chem_e_cross.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'You have already registered, click {<a href="https://azeotropy-iitb.github.io/chem-e-cross/">here</a>} to proceed.'
                })
            else:
                # print('hellow world')
                # Create the user:

                # user = User.objects.create_user(
                #     # form.cleaned_data['username'],
                #     form.cleaned_data['email']

                # )

                extendeduser = User_Chem_e_cross()
                extendeduser.first_name = form.cleaned_data['first_name']
                extendeduser.last_name = form.cleaned_data['last_name']
                extendeduser.phone_number = form.cleaned_data['phone_number']
                # extendeduser.alternate_phone_number = form.cleaned_data['alternate_phone_number']
                extendeduser.college = form.cleaned_data['college']
                extendeduser.current_year = form.cleaned_data['current_year']
                # extendeduser.permanent_address = form.cleaned_data['permanent_address']
                extendeduser.state = form.cleaned_data['state']
                extendeduser.email = form.cleaned_data['email']
                extendeduser.pincode = form.cleaned_data['pincode']
                # extendeduser.user = user

                extendeduser.save()
                message = 'You have successfully registered on CA portal'
                return redirect( "https://azeotropy-iitb.github.io/chem-e-cross/")
                # redirect to home page:
                #return redirect('registration_ca:index')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm2()

    return render(request, template, {'form': form})
