
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('Home_page.urls')),
    path('product/', include('Product_page.urls' )),

    path('contact_us/', include('Contact_us_page.urls')),

    path('about_us/', include('About_us_page.urls')),

    path('admin/', admin.site.urls),
]
