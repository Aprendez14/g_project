from django.forms import widgets
from rest_framework import serializers
from infos.models import Info

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('id', 'name', 'golden_badges', 'silver_badges', 'bronze_badges', 'points', 'level', 'percent_in_level')#, 'last_login')
