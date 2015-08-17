from django.forms import widgets
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'name', 'golden_badges', 'silver_badges', 'bronze_badges', 'points', 'level', 'percent_in_level')#, 'last_login')
