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


def home(request):
    return render(request,'index.html') 
 
def index(request):
    return render(request,'index.html') 
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
            user.save()

            # Send email
            send_mail(
                'Welcome to Our Site',
                f'Hi {username},\n\nWelcome to our site!',
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


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)


        if user is not None:
            if user.is_staff:  # Checking if the user is an admin
                login(request, user)
                messages.success(request, "Logged In Successfully as Admin!!")
                return redirect('admin1')  # Redirect admin to admin dashboard
            else:
                messages.error(request, "Logged In Successfully as Player!!")
                return redirect('admin1')  # Redirect regular users to home page
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "signin.html")


@login_required
def admin1(request):
    return render(request, "admin1.html")