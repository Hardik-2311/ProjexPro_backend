from rest_framework import serializers
from projexApp.models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"
        

    def validate(self, data):       
        return data
