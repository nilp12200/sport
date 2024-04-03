# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
import uuid
from django.utils.http import urlsafe_base64_decode


def home(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def signout(request):
    return redirect('home')

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
            user.email = token  # Save token in user email field
            user.save()

            # Send email with confirmation link
            confirmation_link = request.build_absolute_uri(reverse('activate', kwargs={'uidb64': urlsafe_base64_encode(force_bytes(user.pk)), 'token': token}))
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

def activate(request, uidb64, token):
    try:
        user_id = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=user_id, email=token)  # Use email field to store token
        user.is_active = True  # Activate user account
        user.save()
        messages.success(request, 'Account activated successfully. You can now login.')
        return redirect('signin')
    except User.DoesNotExist:
        messages.error(request, 'Invalid confirmation link.')
        return redirect('home')  # Redirect to home page if token is invalid

def signin(request):
    return render(request, "signin.html")

def admin1(request):
    return render(request, "admin1.html")
