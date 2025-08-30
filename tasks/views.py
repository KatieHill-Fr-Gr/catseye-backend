from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Task
from projects.models import Project 
from .serializers.common import TaskSerializer
from .serializers.populated import PopulatedTaskSerializer


from django.shortcuts import get_object_or_404


class TaskListView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedTaskSerializer
        return TaskSerializer 

    def get_queryset(self):
        return Task.objects.filter(parent_project_id=self.kwargs['pk'])
    
    def perform_create(self, serializer): 
        serializer.save(parent_project_id=self.kwargs['pk'])


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedTaskSerializer
        return TaskSerializer 

    lookup_field = 'pk'
    lookup_url_kwarg = 'task_pk'

    def get_queryset(self):
        project_pk = self.kwargs['pk']
        get_object_or_404(Project, pk=project_pk) 
        return Task.objects.filter(parent_project_id=project_pk)
    