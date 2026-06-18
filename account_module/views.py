from django.contrib.auth.views import LoginView
from django.views.generic import FormView


# Create your views here.

class loginView(LoginView):
    template_name = 'account_module/login.html'
    success_url = 'home'


class registerView(LoginView):

    template_name = 'account_module/register.html'
    success_url = 'home'