from django.contrib import admin
from .models import SiteSetting,FooterLink,FooterLinkBox,SiteServices


class SiteSettingAdmin(admin.ModelAdmin):

    list_display = ['site_name', 'email','is_main_setting']
    list_filter = ['site_name', 'email']
    list_editable = ['is_main_setting']



class SiteServicesAdmin(admin.ModelAdmin):


    list_display = ['title']



admin.site.register(SiteSetting, SiteSettingAdmin)
admin.site.register(FooterLink)
admin.site.register(FooterLinkBox)
admin.site.register(SiteServices , SiteServicesAdmin)
