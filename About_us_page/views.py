from django.shortcuts import render


def About_Us_page(request):

    context = {

    }
    return render(request,'about_us/about_us.html',context)