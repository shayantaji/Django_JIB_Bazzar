from django.shortcuts import render

from Product_page.models import Product
from site_config.models import SiteSetting,FooterLink,FooterLinkBox

def home_page(request):

    data = SiteSetting.objects.filter(
        is_main_setting=True
    ).first()

    latest_products = Product.objects.filter(
        is_active=True
    ).order_by('-created_date')[:8]

    featured_products = Product.objects.filter(
        is_active=True,
        is_featured=True
    )[:8]

    best_selling_products = Product.objects.filter(
        is_active=True
    ).order_by('-sold_count')[:8]

    top_rated_products = Product.objects.filter(
        is_active=True,
        rating__gt=0
    ).order_by('-rating')[:8]

    context = {
        'site_setting': data,
        'latest_products': latest_products,
        'best_selling_products': best_selling_products,
        'top_rated_products': top_rated_products
    }

    if featured_products.exists():
        context['featured_products'] = featured_products

    return render(request, 'home_page/home_page.html', context)
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