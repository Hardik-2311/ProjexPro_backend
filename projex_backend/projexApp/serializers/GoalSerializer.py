from rest_framework import serializers
from projexApp.models import Goal

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'
    def validate(self, data):
        return data
