from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView


class ProductPage(TemplateView):

    template_name = "product_page/product_page.html"
