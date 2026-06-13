from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [

    path('', include('Home_page.urls')),
    path('products/', include('Product_page.urls' )),

    path('contact_us/', include('Contact_us_page.urls')),

    path('about_us/', include('About_us_page.urls')),

    path('admin/', admin.site.urls),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)