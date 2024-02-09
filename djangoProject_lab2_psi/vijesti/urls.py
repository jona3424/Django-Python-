"""
URL configuration for djangoProject_lab2_psi project.

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
from .views import *
urlpatterns = [
    path('',index,name='home'),
    path('login/', login_req, name='login'),
    path('logout/', logout_req, name='logout'),
    path('register/', register_req, name='register'),
    path('kreiranje/', creatingVijest, name='kreiranje'),
    path('delete/', deleteVijest, name='delete'),
]
