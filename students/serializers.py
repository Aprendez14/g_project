from django.forms import widgets
from rest_framework import serializers
from students.models import Student, Action

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'player_type', 'learning_style', 'golden_badges', 'silver_badges', 'bronze_badges', 'points', 'level', 'percent_in_level')
        #fields = ('url', 'id', 'name', 'player_type', 'learning_style', 'golden_badges', 'silver_badges', 'bronze_badges', 'points', 'level', 'percent_in_level', 'last_login')


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('id', 'name', 'description', 'consequence')
        #fields = ('url', 'id', 'name', 'description', 'consequence')
