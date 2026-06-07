from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProductPage.as_view(), name='product_page'),

    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail')
]