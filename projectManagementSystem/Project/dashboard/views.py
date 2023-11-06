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

    if user.user_type == 'owner':
        # Redirect the owner to the owner dashboard
        return render(request,'dashboard_owner.html')
    
    elif user.user_type == 'manager':
        # Redirect the manager to the manager dashboard
        return render(request,'dashboard_manager.html')
    
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
        projects = project.objects.filter(ManagerEmail=user.email)
        return render(request,'manager_view_project.html',{'project': projects})
        
    elif user.user_type == 'employee':
        projects = project.objects.filter(employeeEmail=user.email)
        return render(request,'employee_view_project.html',{'project': projects})

#owner    
@login_required    
def edit_project(request,project_id):
    
    owner_instance = owner.objects.get(email=request.user.email)
    managers = manager.objects.filter(company_name=owner_instance)
    projects = project.objects.get(projectID=project_id)
    user=request.user
    
    if not user.user_type != owner:
        messages.error(request, "Only owners can edit projects.")
        return redirect('Logout')
    
    if request.method == 'POST':
        project_title = request.POST.get('project_title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        assignee = request.POST['manager'].split('-')
        
        project.projectTitle = project_title
        project.description = description
        project.deadline = deadline
        project.managerName=assignee[0]
        project.managerEmail=assignee[1]
        project.save()

        return redirect('/dashboard/project')  # Redirect to the project details page

    return render(request, 'edit_project.html', {'managers':managers},{'project': project})    




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


