from django.forms import widgets
from rest_framework import serializers
from users.models import User, Action

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'name', 'player_type', 'learning_style', 'golden_badges', 'silver_badges', 'bronze_badges', 'points', 'level', 'percent_in_level')#, 'last_login')

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('url', 'id', 'name', 'description', 'consequence')
