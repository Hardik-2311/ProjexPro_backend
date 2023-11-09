from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from projexApp.models import Goal
from projexApp.serializers import GoalSerializer

class GoalDetail(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "id"
    http_method_names = ["get", "put", "patch", "delete", "post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        goal_instance = self.get_object()
        serializer = self.get_serializer(goal_instance)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        goal_instance = self.get_object()
        serializer = self.get_serializer(goal_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        goal_instance = self.get_object()
        goal_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
