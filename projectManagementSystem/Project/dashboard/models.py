from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from accounts.models import owner
from accounts.models import manager
from accounts.models import employee

class Task(models.Model):
    taskID = models.SlugField(primary_key=True, max_length=32, editable=False)
    title = models.CharField(max_length=64)
    description = models.TextField()
    deadline = models.DateTimeField(blank=True)
    submitted = models.DateTimeField(blank=True)
    completed = models.DateTimeField(blank=True)
    assigned = models.DateTimeField()
    EmployeeName = models.CharField(max_length=30, blank=True)
    EmployeeEmail = models.EmailField(unique=True)
    projectID = models.SlugField(max_length=15)
    ManagerName = models.CharField(max_length=30, blank=True)
    ManagerEmail = models.EmailField(unique=True)
    status = models.CharField(max_length=1, default='N',
        choices=[
            ('I', 'In Progress'),
            ('C', 'Completed'),
            ('R', 'Submitted For Review')
    ])
 
    def __str__(self):
        return self.taskID


class Project(models.Model):
    projectID = models.SlugField(primary_key=True, max_length=15)
    title = models.CharField(max_length=64)
    description = models.TextField()
    deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(blank=True)
    status = models.CharField(max_length=1, default='O',
        choices=[
            ('O', 'Ongoing'),
            ('C', 'Completed'),
    ])
    
    ManagerName = models.CharField(max_length=30, blank=True)
    ManagerEmail = models.EmailField(unique=True)
    
    def __str__(self):
        return self.projectID
    
    