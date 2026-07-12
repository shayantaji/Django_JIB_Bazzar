from django.urls import path, include
from site_config.api_views import SiteSettingApiView
from account_module.api_views import UserApiView
from rest_framework.routers import DefaultRouter

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



urlpatterns = [

    path('site_setting/', include(site_router.urls)),
    path('user/', include(user_router.urls)),

]