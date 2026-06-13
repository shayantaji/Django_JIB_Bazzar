from django.contrib import admin
from .models import Product, ProductCategory, ProductGallery


# Register your models here.

class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 5


class ProductAdmin(admin.ModelAdmin):

    list_filter = ['category', 'is_active',]
    list_display = ['title', 'price', 'is_active']
    list_editable = ['price', 'is_active']
    inlines = [ProductGalleryInline]



class ProductCategoryAdmin(admin.ModelAdmin):

    list_display = ['title', 'is_active']
    list_editable = ['is_active']




admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)