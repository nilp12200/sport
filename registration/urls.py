"""
URL configuration for registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('',views.home,name='home'),
    path('signup/',views.signuppage,name='signuppage'),
    path('signout',views.signout,name='signout'),
    path('signin',views.signin,name='signin'),
    path('admin1', views.admin1, name='admin1'),
    # path('signupparent/',views.signupparent,name='signupparent'),
    # path('signupchild/',views.signupchild,name='signupchild'),
    # path('loginchild/signupchild',views.signupchild,name='signupchild'),
    # path('loginparent/signupparent',views.signupchild,name='signupchild'),
    
    # path('loginpage/',views.loginpage,name='loginpage'),
    # path('loginparent/',views.loginparent,name='loginparent'),
    # path('signupparent/loginparent',views.loginparent,name='loginparent'),
    # path('loginchild/',views.loginchild,name='loginchild'),
    # path('/loginparent/',views.loginparent,name='loginparent'),
    # path('home1/',views.home1,name='home1'),
    # path('child/',views.childpage,name='childpage'),
    # path('loginparent/parent.html',views.parentpage,name='parentpagepage'),
    
     
    
    # path('Pay', views.homepage1, name='index'),
    #  path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
     path('admin/', admin.site.urls),
    
    
    
]
