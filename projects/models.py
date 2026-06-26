from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
class Task(models.Model):
    title = models.CharField(max_length=100)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    status = models.CharField(max_length=20, choices=[('todo', 'Todo'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
