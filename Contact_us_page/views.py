from django.shortcuts import render

from django.shortcuts import render

from site_config.models import SiteSetting


def Contact_Us_page(request):
    data = SiteSetting.objects.first()
    context = {
        'site_setting': data
    }
    return render(request, 'contact_us/contact_us.html', context)