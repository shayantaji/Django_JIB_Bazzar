from django.db import models


class FeedbackBox(models.Model):
    subject = models.CharField(max_length=100,verbose_name='موضوع')
    text = models.TextField(verbose_name='متن پیام')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'انتقاد'
        verbose_name_plural = 'صندوق انتقادات و پیشنهادات'



class CommunicationBox(models.Model):
    name=models.CharField(max_length=100,verbose_name='نام')
    email=models.EmailField(verbose_name='ایمیل')
    massage=models.TextField(verbose_name='پیام کاربر')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'پیام مشتری'
        verbose_name_plural = 'صندوق پیام های مشتری'