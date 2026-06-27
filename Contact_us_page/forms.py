from django import forms
from Contact_us_page.models import FeedbackBox





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