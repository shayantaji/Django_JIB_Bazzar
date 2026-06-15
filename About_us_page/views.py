from django.shortcuts import render
from site_config.models import SiteSetting
def About_Us_page(request):
    data=SiteSetting.objects.first()
    context = {
        'site_setting': data,
    }
    return render(request,'about_us/about_us.html',context)