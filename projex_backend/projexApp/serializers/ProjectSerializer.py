from rest_framework import serializers
from projexApp.models import Project
from .UserSerializer import UserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields ='__all__'
