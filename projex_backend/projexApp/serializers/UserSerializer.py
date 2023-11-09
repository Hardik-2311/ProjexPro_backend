from projexApp.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'is_active', 'is_superuser', 'profile_pic', 'email', 'enrolment_no']
        partial = True
