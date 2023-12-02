from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from accounts.models import *
import os
    
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
    taskIDs = models.ManyToManyField('Task', related_name='projects', blank=True)
    chat=models.CharField(max_length=15,blank=True)
    def __str__(self):
        return self.projectTitle
    
class message(models.Model):
    chatID = models.SlugField(primary_key=True, max_length=15)
    prevMessage = models.CharField(max_length=15, blank=True)
    text = models.TextField()
    senderName = models.CharField(max_length=30, blank=True)
    senderEmail = models.EmailField()
    role = models.CharField(
        max_length=1,
        default='E',
        choices=[
            ('E', 'Employee'),
            ('M', 'Manager'),
            ('O', 'Owner'),
        ]
    )
    def __str__(self):
        return self.chatID



class Task(models.Model):
    taskID = models.SlugField(primary_key=True, max_length=32, editable=False)
    taskTitle = models.CharField(max_length=64)
    description = models.TextField()
    deadline = models.DateTimeField()
    submitted = models.DateTimeField(blank=True, null=True)
    completed = models.DateTimeField(blank=True, null=True)
    assignedDate = models.DateTimeField()
    employeeName = models.CharField(max_length=30, blank=True)
    employeeEmail = models.EmailField()
    projectID = models.ForeignKey(project, on_delete=models.CASCADE)
    managerName = models.CharField(max_length=30, blank=True)
    managerEmail = models.EmailField()
    late = models.BooleanField(default=False)
    decline = models.BooleanField(default=False)
    
    
    status = models.CharField(max_length=1, default='I',
        choices=[
            ('I', 'In Progress'),
            ('C', 'Completed'),
            ('R', 'Submitted For Review')
    ])
 
    def __str__(self):
        return self.taskID

    




    
    