from django.contrib.auth.views import LoginView
from django.template.defaultfilters import first
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import FormView
from account_module.forms import RegisterForm
from account_module.models import User
from utils.email_service import send_email


# Create your views here.

class RegisterView(FormView):

    template_name = 'account_module/register.html'
    success_url = reverse_lazy('home')
    form_class = RegisterForm

    def form_valid(self, form):
        form_email = form.cleaned_data['email']
        form_username = form.cleaned_data['user_name']
        form_password = form.cleaned_data['password']
        check_user : bool = User.objects.filter(email__iexact=form_email).exists()
        if check_user:
            form.add_error('email','کاربری با این ایمیل وجود دارد')
            return self.form_invalid(form)
        new_user = User(
            first_name=form_username,
            email=form_email,
            username=form_username,
            is_active=False,
            email_active_code=get_random_string(72)

        )
        new_user.set_password(form_password)
        new_user.save()
        send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/email_active_code.html')
        return super().form_valid(form)

class LoginView(FormView):
    pass