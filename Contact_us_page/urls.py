from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [

    path('', views.Contact_Us_page, name='contact_us'),


    path('feedback-massage/', views.FeedbackMassageView.as_view(), name='feedback_massage'),


    path ('Communication-Massage/',views.CommunicationMassageView.as_view(), name='Communication_Massage'),

]