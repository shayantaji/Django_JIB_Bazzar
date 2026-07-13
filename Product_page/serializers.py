from rest_framework import serializers
from .models import Product,ProductCategory,ProductGallery




class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id','title','slug','image','short_description','price','rating',
        ]


class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = [
            'id',
            'image',
        ]


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'title',
            'url_title',
        ]



class ProductCategoryDetailSerializer(serializers.ModelSerializer):

    products_category = ProductListSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'title',
            'url_title',
            'products_category',
        ]



class ProductDetailSerializer(serializers.ModelSerializer):

    category = ProductCategorySerializer(
        read_only=True
    )

    gallery = ProductGallerySerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Product

        fields = [
            'id','title','slug','image','short_description','description','price','inventory','sold_count','rating',
            'category','gallery','is_featured','is_active','created_date'
                  ]