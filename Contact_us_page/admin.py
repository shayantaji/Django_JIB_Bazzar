from django.contrib import admin
from .models import FeedbackBox
# Register your models here.

class FeedbackBoxAdmin(admin.ModelAdmin):

    list_display = ['text',  'subject']
    list_editable = ['subject']


admin.site.register(FeedbackBox)