from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView

from Product_page.models import Product


class ProductPage(ListView):
    model = Product
    template_name = "product_page/product_page.html"
    context_object_name = "products"
    ordering = ['-rating']
    paginate_by = 6

    def get_queryset(self):
        base_query = super(ProductPage, self).get_queryset()
        data=base_query.filter(is_active=True)

        return data



class ProductDetailView(DetailView):
    model = Product
    template_name = "product_page/product_detail_page.html"
    context_object_name = "product"


