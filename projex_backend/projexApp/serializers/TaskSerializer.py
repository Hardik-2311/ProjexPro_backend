from rest_framework import serializers
from projexApp.models import Task
class taskSerializer(serializers.ModelSerializer):
   class Meta:
      model=Task
      fields='__all__' 