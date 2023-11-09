from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from projexApp.models import Task
from projexApp.serializers import TaskSerializer

class TaskDetailViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = []
    lookup_url_kwarg = "id"
    http_method_names = ["get", "put", "patch", "delete", "post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        task_instance = self.get_object()
        serializer = self.get_serializer(task_instance)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        task_instance = self.get_object()
        serializer = self.get_serializer(task_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        task_instance = self.get_object()
        task_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        task_instance = self.get_object()
        serializer = self.get_serializer(task_instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
