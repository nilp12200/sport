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


def home(request):
    return render(request,'index.html') 
 
def index(request):
    return render(request,'index.html') 
def signout(request):
    return redirect('home') 


def signuppage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('Pass1')
        pass2=request.POST.get('Pass2')
        my_user = User.objects.create_user(username=username, email=email, password=pass1)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.save()

        return redirect('signin')
        # return HttpResponse("user has been created successuful")
        # print(uname,email,password)
    return render( request,'signuppage.html')


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
