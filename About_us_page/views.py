from django.shortcuts import render
from Contact_us_page.forms import FeedbackBoxForm
from site_config.models import SiteSetting, SiteServices, SocialMediaServices


def About_Us_page(request):
    data=SiteSetting.objects.filter(is_main_setting=True).first()
    service = SiteServices.objects.filter(site=data)


    SocialMedia = SocialMediaServices.objects.filter(site=data).first()

    context = {
        'site_setting': data,
        'services': service,
        'form': FeedbackBoxForm(),
        'SocialMedia': SocialMedia
    }

    return render(request,'about_us/about_us.html',context)