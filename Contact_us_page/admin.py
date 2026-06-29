from django.contrib import admin
from .models import FeedbackBox,CommunicationBox


class FeedbackBoxAdmin(admin.ModelAdmin):

    list_display = ['text',  'subject']
    list_editable = ['subject']


class CommunicationBoxAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']



admin.site.register(FeedbackBox, FeedbackBoxAdmin)
admin.site.register(CommunicationBox, CommunicationBoxAdmin)
