from django.shortcuts import render
from site_config.models import SiteSetting,SiteServices
def About_Us_page(request):
    data=SiteSetting.objects.filter(is_main_setting=True).first()
    service = SiteServices.objects.filter(site=data)
    context = {
        'site_setting': data,
        'services': service,
    }
    return render(request,'about_us/about_us.html',context)