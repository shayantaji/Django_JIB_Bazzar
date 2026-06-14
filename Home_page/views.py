from django.shortcuts import render
from site_config.models import SiteSetting,FooterLink,FooterLinkBox

def home_page(request):
    data: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': data,
    }
    return render(request,"home_page/home_page.html",context)


def header_site_component(request):
    data : SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {'site_setting':data}
    return render(request,"main/header_site_component.html",context)


def footer_site_component(request):
    data: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link = FooterLinkBox.objects.all()
    context = {
        'site_setting': data,
        'footer_links': footer_link
               }

    return render(request,"main/footer_site_component.html",context)