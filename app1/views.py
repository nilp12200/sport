from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes




def home(request):
    return render(request,'index.html') 
 
def index(request):
    return render(request,'index.html') 
def signout(request):
    return redirect('home') 


import uuid  # For generating unique tokens
from django.urls import reverse

def signuppage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('Pass1')
        pass2 = request.POST.get('Pass2')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return redirect('signuppage')

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, 'Passwords do not match. Please try again.')
            return redirect('signuppage')

        # Create the user
        try:
            user = User.objects.create_user(username=username, email=email, password=pass1)
            user.first_name = fname
            user.last_name = lname
            
            # Generate unique token for confirmation
            token = str(uuid.uuid4())
            user.confirmation_token = token  # Save token in user model
            user.save()

            # Send email with confirmation link
            confirmation_link = request.build_absolute_uri(reverse('confirm_account', kwargs={'token': token}))
            send_mail(
                'Welcome to Our Site',
                f'Hi {username},\n\nWelcome to our site! Please click the following link to confirm your account: {confirmation_link}',
                'sender@example.com',
                [email],
                fail_silently=False,
            )

            messages.success(request, 'Account created successfully. Check your email for verification.')
            return redirect('signin')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
            return redirect('signuppage')

    return render(request, 'signuppage.html')


def confirm_account(request, token):
    try:
        user = User.objects.get(confirmation_token=token)
        user.is_active = True  # Activate user account
        user.save()
        messages.success(request, 'Account activated successfully. You can now login.')
        return redirect('signin')
    except User.DoesNotExist:
        messages.error(request, 'Invalid confirmation link.')
        return redirect('home')  # Redirect to home page if token is invalid



def signin(request):
    return render(request, "signin.html")

@login_required
def admin1(request):
    return render(request, "admin1.html")
