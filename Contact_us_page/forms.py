from importlib.metadata import requires

from django import forms
from Contact_us_page.models import FeedbackBox, CommunicationBox


class FeedbackBoxForm(forms.ModelForm):
    class Meta:
        model = FeedbackBox
        fields = ['subject', 'text']

        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'feedback-input',
                'placeholder': 'عنوان پیام',
            }),

            'text': forms.Textarea(attrs={
                'class': 'feedback-textarea',
                'placeholder': 'انتقاد، پیشنهاد یا نظر خود را بنویسید...',
                'rows': 5,
            }),

        }
        error_messages = {
            'subject': {

                'required': 'لطفا موضوع خود را وارد کنید'
            },
            'text': {

                'required': 'لطفا توضیحات خود را وارد کنید'

            }
        }

class CommunicationForm(forms.ModelForm):
    class Meta:
        model = CommunicationBox
        fields = ['name', 'email', 'massage']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'feedback-input',
                'placeholder': 'نام شما',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'feedback-input',
                'placeholder': 'ایمیل شما',
            }),

            'massage': forms.Textarea(attrs={
                'class': 'feedback-textarea',
                'placeholder': 'پیام شما',
                'rows': 5,
            }),
        }
        error_messages = {
            'name': {

                'required': 'لطفا نام خود را وارد کنید'
            },
            'email': {

                'required': 'لطفا ایمیل خود را وارد کنید'

            },
            'massage': {

                'required': 'لطفا سوال خود را وارد کنید'

            }
        }