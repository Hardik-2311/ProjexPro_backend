from rest_framework import serializers
from projexApp.models import Project
from .UserSerializer import UserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    project_members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'description', 'wiki', 'created_time', 'project_members', 'creator']
        read_only_fields = ['id', 'created_time', 'project_members', 'creator']
