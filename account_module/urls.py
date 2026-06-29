from django.urls import path
from  . import  views

urlpatterns = [

    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('activate-account/<email_active_code>', views.ActivateAccountView.as_view(), name='activate_account'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password/<email_active_code>', views.PasswordResetView.as_view(), name='reset_password'),
    path('activate-massage/', views.ActivateMassageView.as_view(), name='activate_massage'),
    path('notactivate-massage/', views.NotActivateMassageView.as_view(), name='not_activate_massage'),
    path('resend-email/', views.ResendEmailView.as_view(), name='resend_email'),
    path('send-email-succses', views.SendEmailSuccessView.as_view(), name='send_email_success'),

]