from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from accounts.models import *
    
class project(models.Model):
    projectID = models.SlugField(primary_key=True, max_length=15)
    projectTitle = models.CharField(max_length=64)
    description = models.TextField()
    deadline = models.DateTimeField()
    created = models.DateTimeField()
    completed = models.DateTimeField(blank=True, null=True)
    managerName = models.CharField(max_length=50,blank=True)
    managerEmail = models.EmailField(unique=False)
    ownerName = models.CharField(max_length=50,blank=True)
    ownerEmail = models.EmailField(unique=False)
    status = models.CharField(
        max_length=1,
        default='O',
        choices=[
            ('O', 'Ongoing'),
            ('C', 'Completed'),
        ]
    )
    def __str__(self):
        return self.projectTitle
    



class Task(models.Model):
    taskID = models.SlugField(primary_key=True, max_length=32, editable=False)
    taskTitle = models.CharField(max_length=64)
    description = models.TextField()
    deadline = models.DateTimeField(blank=False)
    submitted = models.DateTimeField(blank=True)
    completed = models.DateTimeField(blank=True)
    assignedDate = models.DateTimeField()
    EmployeeName = models.CharField(max_length=30, blank=True)
    EmployeeEmail = models.EmailField(unique=True)
    projectID = models.ForeignKey(project, on_delete=models.CASCADE)
    #ManagerName = models.CharField(max_length=30, blank=True)
    ManagerEmail = models.EmailField(unique=True)
    status = models.CharField(max_length=1, default='I',
        choices=[
            ('I', 'In Progress'),
            ('C', 'Completed'),
            ('R', 'Submitted For Review')
    ])
 
    def __str__(self):
        return self.taskID




    
    