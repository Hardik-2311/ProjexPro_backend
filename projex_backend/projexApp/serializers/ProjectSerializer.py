from .UserSerializer import UserSerializer
from projexApp.models import Project
from rest_framework import serializers
class ProjectModelSerializer(serializers.ModelSerializer):
    project_members=UserSerializer(many=True)
    class Meta:
        model = Project
        fields = ['project_id','project_name','description','wiki','project_members','creator'] 
        partial=True