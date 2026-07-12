from rest_framework import viewsets
from site_config.serializers import SiteSettingSerializer
from . models import SiteSetting

class SiteSettingApiView(viewsets.ModelViewSet):
    queryset = SiteSetting.objects.all()
    serializer_class = SiteSettingSerializer