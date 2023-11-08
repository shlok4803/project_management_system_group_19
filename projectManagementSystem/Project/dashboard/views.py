from django.shortcuts import render,redirect
from django.urls import reverse
from accounts.models import *
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from accounts.views import *
from .models import *
from datetime import datetime
from accounts.models import *
from accounts.models import manager
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone



# Owner, PM and Employee
@login_required
def dashboard(request):
  
    user=request.user
    projects=None
    
    
    if user.user_type == 'owner':
        # Redirect the owner to the owner dashboard
        projects = project.objects.all()
        recent_projects = projects.order_by('-created')[:3]
        ongoing_count = project.objects.filter(status='O').count()
        completed_count = project.objects.filter(status='C').count()
        return render(request, 'dashboard_owner.html', {'projects': projects, 'ongoing_count': ongoing_count, 'completed_count': completed_count,'recent_projects':recent_projects})
    
    elif user.user_type == 'manager':
        # Redirect the manager to the manager dashboard
        projects = project.objects.filter(managerEmail=user.email)
        recent_projects = projects.order_by('-created')[:3]
        ongoing_count = projects.filter(status='O').count()
        completed_count = projects.filter(status='C').count()
        return render(request, 'dashboard_manager.html', {'projects': projects, 'ongoing_count': ongoing_count, 'completed_count': completed_count,'recent_projects':recent_projects})
    
    elif user.user_type == 'employee':
        # Redirect the employee to the employee dashboard
        return render(request,'dashboard_employee.html')
    
    else:
       return render(request, 'access_denied.html')

    
  
#owner
@login_required
def CreateProject(request):
    
    owner_instance = owner.objects.get(email=request.user.email)
    managers = manager.objects.filter(company_name=owner_instance)
    
    user=request.user
    if not user.user_type != owner:
        messages.error(request, "Only owners can create projects.")
        return redirect('Logout')
    
    
    
    if request.method == 'POST':
        csrf_token = request.POST.get('csrfmiddlewaretoken')
        projectTitle = request.POST.get('project_title')
        description = request.POST.get('description')
        assignee = request.POST['manager'].split('-')
        deadline = request.POST.get('deadline')
        timestamp = datetime.now()
        
        
        Project = project(
            projectID="PRJ"+timestamp.strftime("%d%m%y%H%M%S"),
            projectTitle=projectTitle,
            description=description,
            deadline=deadline,
            created=timestamp,
            managerName=assignee[0],
            managerEmail=assignee[1],
            status='O',
            ownerName = user.first_name,
            ownerEmail = user.email,
            chatID='NULL'
        )
        messages.success(request, 'Project Created Successfully.')
        Project.save()
        
        return redirect('/dashboard/project')  # Redirect to a project list view
    
    #managers = manager.objects.get(company_name=user.company_name)
    return render(request, 'create_project.html',{'managers':managers})

@login_required
def view_project(request):
    user = request.user
    projects = None
    
    
    if user.user_type == 'owner':
        
        # Owners can view all projects.
        projects = project.objects.all()
        
        return render(request,'owner_view_project.html',{'projects': projects})
        
    elif user.user_type == 'manager': 
        # Managers and employees can view projects they are assigned to.
        projects = project.objects.filter(managerEmail=user.email)
        return render(request,'manager_view_project.html',{'project': projects})
        
    elif user.user_type == 'employee':
        
        curTasks = Task.objects.filter(EmployeeEmail=user.email).values()
        projects = project.objects.filter(projectID__in=curTasks)
        return render(request,'employee_view_project.html',{'project': projects})

#owner    
@login_required    
def edit_project(request,project_id):
    
    owner_instance = owner.objects.get(email=request.user.email)
    managers = manager.objects.filter(company_name=owner_instance)
    project_instance = project.objects.get(projectID=project_id)
    user=request.user
    
    if not user.user_type != owner:
        messages.error(request, "Only owners can edit projects.")
        return redirect('Logout')
    
    if request.method == 'POST':
        project_title = request.POST.get('project_title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        assignee = request.POST['manager'].split('-')
        status = request.POST.get('projectstatus')
        print(status)
        
        
        project_instance.projectTitle = project_title
        project_instance.description = description
        project_instance.deadline = deadline
        project_instance.managerName=assignee[0]
        project_instance.managerEmail=assignee[1]

        if status == 'completed':
            project_instance.status='C'
            project_instance.completed=datetime.now()
        
        else:
            project_instance.status='O'
            project_instance.completed=None
        
        project_instance.save()

        return redirect('/dashboard/project')  # Redirect to the project details page

    return render(request, 'edit_project.html', {'managers':managers,'project': project_instance})    


#Project Chat
@login_required    
def viewChat(request,project_id):
    curProject=project.objects.get(projectID=project_id)
    curManager = manager.objects.get(email=curProject.managerEmail)
    curOwner = owner.objects.get(email=curProject.ownerEmail)
    curTasks = Task.objects.filter(projectID=project_id)
    curEmployees = employee.objects.filter(taskID__in=curTasks)
    user=request.user
    curRole='N'


    if user==curOwner:
        curRole='O'
    if user==curManager:
        curRole='M'
    if user in curEmployees:
        curRole='E'


    if curRole=='N':
        messages.error(request, "You don't have access to this page")
        return redirect('Logout')
    
    if request.method == 'POST':
        csrf_token = request.POST.get('csrfmiddlewaretoken')
        newText = request.POST.get('Text')
        timestamp = datetime.now()
        newChatID="CHT"+timestamp.strftime("%d%m%y%H%M%S")
        
        newMessage = project(
            chatID=newChatID,
            prevMessage=curProject.chatID,
            text=newText,
            senderName=user.first_name,
            senderEmail=user.email,
            role=curRole
        )
        curProject.chatID=newChatID
        newMessage.save()
        
        return redirect('/dashboard/project/chat')

    allMessage=[]
    curChatID=curProject.chatID
    while curChatID!='NULL':
        allMessage.append(message.objects.get(chatID=curChatID))
        curChatID=curChatID.prevMessage
    allMessage.reverse()

    return render(request, 'view_chats.html', {'project':curProject,'messages': allMessage})





#Project Manager
@login_required
def CreateTask(request, projectID):
    try: 
        project = project.objects.get(projectID=projectID)
    except:
        raise ObjectDoesNotExist
    
    user = request.user
    
    if not user.user_type == 'manager':
        raise PermissionDenied

    if request.method == "POST":
        assignee = request.POST['employee'].split('-')
        if request.POST.get('taskID', ''):
            task = Task.objects.get(taskID=request.POST['taskID'])
            task.taskTitle = request.POST['title']
            task.description = request.POST['description']
            task.deadline = request.POST['deadline']
            task.EmployeeName = assignee[0]
            task.EmployeeEmail=assignee[1]
            task.save()
            messages.success(request, 'Task updated successfully.')
            return redirect(reverse("TaskDashboard", kwargs={"taskID": task.taskID}))
        timestamp = datetime.now()  
        if not task.taskTitle or not task.description or not task.Employee or not task.deadline:
            messages.error(request, "Please fill out all required fields.")  
             
        else:  
            task = Task(
                taskID="TSK"+timestamp.strftime("%d%m%y%H%M%S"),
                taskTitle=request.POST['title'],
                description=request.POST['description'],
                EmployeeName=assignee[0],
                deadline=request.POST['deadline'],
                assigned=timestamp,
                projectID=projectID,
                ManagerEmail= project.managerEmail,
                status='I'
            )
            task.save()
            messages.success(request, 'Task '+ task.taskID + ' created successfully.')
            return redirect('your_task_dashboard_name', taskID=task.taskID)

    return redirect(reverse("ProjectDashboard", kwargs={"projectID": projectID}))


@login_required
def view_profile(request):
    return render(request,'profile.html')


