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