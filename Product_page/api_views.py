from rest_framework import viewsets
from Product_page.models import Product, ProductCategory, ProductGallery
from Product_page.serializers import ProductDetailSerializer, ProductCategorySerializer, ProductGallerySerializer,ProductListSerializer


class ProductApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    def get_serializer_class(self):

        if self.action == "list":
            return ProductListSerializer

        return ProductDetailSerializer

class ProductCategoryApiView(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductGalleryApiView(viewsets.ModelViewSet):
    queryset = ProductGallery.objects.all()
    serializer_class = ProductGallerySerializer
