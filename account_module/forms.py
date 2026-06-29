from django.core.exceptions import ValidationError
from django import forms
from django.core import validators



class RegisterForm(forms.Form):

    user_name = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={
            'class': 'input100',
            'placeholder': 'نام کاربری خود را وارد کنید',
            'name': 'username'
        }),  error_messages={
        'required': 'پر کردن این فیلد اجباری است',
    }
    )

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'input100',
            'placeholder': 'ایمیل خود را وارد کنید',
            'name': 'email'
        }),
        error_messages={
        'required': 'پر کردن ایمیل اجباری است',
        'invalid': 'ایمیل معتبر نیست',
    },
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator(),
        ]
    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'input100',
            'placeholder': 'رمز عبور خود را وارد کنید',
            'name': 'pass'
        }),
    error_messages={
        'required': 'رمز عبور الزامی است',
    },
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'input100',
            'placeholder': 'تکرار رمز عبور خود را وارد کنید',
            'name': 'confirm_pass'
        }),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError('کلمه عبور با تکرار آن مفایرت دارد')
        return cleaned_data


class LoginForm(forms.Form):
    email_username = forms.CharField(
        label='نام کاربری یا حساب ایمیل خود را وارد کنید',
        widget=forms.TextInput(attrs={
            'class': 'input100',
            'placeholder': 'نام کاربری یا ایمیل',
            'name': 'username'
        }), error_messages={
            'required': 'پر کردن این فیلد اجباری است',
        },
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'input100',
            'placeholder': 'رمز عبور خود را وارد کنید',
            'name': 'pass'
        }),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'input100',
            'placeholder': 'ایمیل خود را وارد کنید',
            'name': 'email'
        }),
        error_messages={
            'required': 'پر کردن ایمیل اجباری است',
            'invalid': 'ایمیل معتبر نیست',
        },
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator(),
        ]
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'input100',
            'placeholder': 'رمز عبور خود را وارد کنید',

        }),
        error_messages={
            'required': 'رمز عبور الزامی است',
        },
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'input100',
            'placeholder': 'تکرار رمز عبور خود را وارد کنید',

        }),
        error_messages={
            'required': 'تکرار رمز عبور خود را وارد کنید',
        },
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError('کلمه عبور با تکرار آن مفایرت دارد')
        return cleaned_data
