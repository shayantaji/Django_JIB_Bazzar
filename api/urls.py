from itertools import product

from django.urls import path, include

from Product_page.serializers import ProductGallerySerializer
from site_config.api_views import SiteSettingApiView
from account_module.api_views import UserApiView
from Product_page.api_views import ProductApiView,ProductCategoryApiView,ProductGalleryApiView
from rest_framework.routers import DefaultRouter
#region router
site_router = DefaultRouter()
site_router.register(
    '',
    SiteSettingApiView,
    basename='site-setting'
)


user_router = DefaultRouter()
user_router.register(
    '',
    UserApiView,
    basename='user'
)


product_router = DefaultRouter()
product_router.register(
    '',
    ProductApiView,
    basename='peoduct'
)


product_category_router = DefaultRouter()
product_category_router.register(
    '',
    ProductCategoryApiView,
    basename='product_category'
)
product_gallery_router = DefaultRouter()
product_gallery_router.register(
    '',
    ProductGalleryApiView,
    basename='product_gallery'
)



#endregion


urlpatterns = [

    path('site_setting/', include(site_router.urls)),
    path('user/', include(user_router.urls)),
    path('product/', include(product_router.urls)),
    path('product_category/', include(product_category_router.urls)),
    path('product_gallery/', include(product_gallery_router.urls)),
]