from rest_framework import serializers
from projexApp.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('created_time', 'time_added', 'project_id')
