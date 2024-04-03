# urls.py
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('signup/',views.signuppage,name='signuppage'),
    path('signout/',views.signout,name='signout'),
    path('signin/',views.signin,name='signin'),
    path('admin1/', views.admin1, name='admin1'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
