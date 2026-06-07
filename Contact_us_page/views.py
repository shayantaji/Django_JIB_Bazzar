from django.shortcuts import render

from django.shortcuts import render


def Contact_Us_page(request):
    context = {

    }
    return render(request, 'contact_us/contact_us.html', context)