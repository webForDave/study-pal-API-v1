from rest_framework import serializers 
from .models import Goal

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["title", "description", "priority", "deadline"]
        model = Goal