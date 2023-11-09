from rest_framework import viewsets
from projexApp.models import Feedback
from projexApp.serializers import FeedbackSerializer
from rest_framework.response import Response
from rest_framework import status

class FeedbackDetailViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        feedback_instance = self.get_object()
        serializer = self.get_serializer(feedback_instance)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        feedback_instance = self.get_object()
        serializer = self.get_serializer(feedback_instance, data=request.data, partial=True)

        if serializer.is_valid():
            if feedback_instance.content != serializer.validated_data["content"]:
                serializer.validated_data["is_edited"] = True

            self.perform_update(serializer)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        feedback_instance = self.get_object()
        feedback_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
