from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [
path('', views.About_Us_page, name='contact_us'),

]