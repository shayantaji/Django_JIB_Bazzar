from django.contrib.auth.views import LogoutView
from django.urls import path
from  . import  views

urlpatterns = [

    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('activate-account/<email_active_code>', views.ActivateAccountView.as_view(), name='activate_account'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]