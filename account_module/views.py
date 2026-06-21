from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import FormView
from account_module.forms import RegisterForm, LoginForm
from account_module.models import User
from utils.email_service import send_email
from django.contrib.auth import login, logout


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
    template_name = 'account_module/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):

        email_username = form.cleaned_data['email_username']
        password = form.cleaned_data['password']

        user = User.objects.filter(
            Q(username__iexact=email_username) |
            Q(email__iexact=email_username)
        ).first()

        if user is None:
            form.add_error(
                'email_username',
                'کاربری بااین نام کاربری یا ایمیل یافت نشد'
            )
            return self.form_invalid(form)

        if not user.is_active:
            form.add_error(
                'email_username',
                'حساب کاربری شما هنوز فعال نشده است'
            )
            return self.form_invalid(form)

        if not user.check_password(password):
            form.add_error(
                'password',
                'رمز عبور وارد شده صحیح نیست'
            )
            return self.form_invalid(form)

        login(self.request, user)

        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)



class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo: show success message to user
                return redirect(reverse('home'))
            else:
                # todo: show your account was activated message to user
                pass
        raise Http404

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))
