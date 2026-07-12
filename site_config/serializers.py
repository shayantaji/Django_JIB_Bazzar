from rest_framework import serializers
from site_config.models import SiteSetting


class SiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = '__all__'