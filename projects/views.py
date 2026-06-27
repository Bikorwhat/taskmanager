from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from .permissions import IsProjectOwner
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsProjectOwner]
    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
  
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) 
    
class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    def get_queryset(self):
        queryset=(Task.objects.filter(project__owner=self.request.user
        ) | Task.objects.filter(assigned_to=self.request.user)).order_by('created_at')
        
        status=self.request.query_params.get('status')
        if status:
            queryset=queryset.filter(status=status)
            
        project_id=self.request.query_params.get('project')
        if project_id:
            queryset=queryset.filter(project=project_id)
        return queryset
    def perform_create(self, serializer):
        serializer.save()
    