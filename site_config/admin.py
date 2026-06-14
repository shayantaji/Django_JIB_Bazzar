from django.contrib import admin
from .models import SiteSetting,FooterLink,FooterLinkBox


class SiteSettingAdmin(admin.ModelAdmin):

    list_display = ['site_name', 'email']
    list_filter = ['site_name', 'email']
    list_editable = ['is_main_setting']















admin.site.register(SiteSetting)
admin.site.register(FooterLink)
admin.site.register(FooterLinkBox)

