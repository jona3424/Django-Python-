from django.contrib import admin
from django.urls import path

from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('<int:vijest_id>',vijest, name='vijest'),

]
