from django.shortcuts import render, redirect
from Contact_us_page.forms import FeedbackBoxForm
from site_config.models import SiteSetting, SiteServices, SocialMediaServices


def About_Us_page(request):
    data=SiteSetting.objects.filter(is_main_setting=True).first()
    service = SiteServices.objects.filter(site=data)
    SocialMedia = SocialMediaServices.objects.filter(site=data).first()

    if request.method == "POST":
        form = FeedbackBoxForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("feedback_massage")
    else:
        form = FeedbackBoxForm()


    context = {
        'site_setting': data,
        'services': service,
        'form': form,
        'SocialMedia': SocialMedia
    }

    return render(request,'about_us/about_us.html',context)