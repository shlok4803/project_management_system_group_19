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
        return render(request, 'owner/dashboard_owner.html', {'projects': projects, 'ongoing_count': ongoing_count, 'completed_count': completed_count,'recent_projects':recent_projects})
    
    elif user.user_type == 'manager':
        # Redirect the manager to the manager dashboard
        projects = project.objects.filter(managerEmail=user.email)
        recent_projects = projects.order_by('-created')[:3]
        ongoing_count = projects.filter(status='O').count()
        completed_count = projects.filter(status='C').count()
        return render(request, 'manager/dashboard_manager.html', {'projects': projects, 'ongoing_count': ongoing_count, 'completed_count': completed_count,'recent_projects':recent_projects})
    
    elif user.user_type == 'employee':
        # Redirect the employee to the employee dashboard
        task_instance = Task.objects.filter(employeeEmail=user.email)
        recent_task = task_instance.order_by('-assignedDate')[:3]
        ongoing_count = task_instance.filter(status='I').count()
        completed_count = task_instance.filter(status='C').count()
        return render(request,'employee/dashboard_employee.html',{'projects': projects, 'ongoing_count': ongoing_count, 'completed_count': completed_count,'recent_tasks':recent_task})
    
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
            ownerEmail = user.email
        )
        messages.success(request, 'Project Created Successfully.')
        Project.save()
        
        return redirect('/dashboard/project')  # Redirect to a project list view
    
    #managers = manager.objects.get(company_name=user.company_name)
    return render(request, 'owner/create_project.html',{'managers':managers})


@login_required
def view_project(request):
    user = request.user
    projects = None
    
    if user.user_type == 'owner': 
        # Owners can view all projects.
        
        projects = project.objects.all() 
        return render(request,'owner/owner_view_project.html',{'projects': projects})
        
    elif user.user_type == 'manager': 
        # Managers can view projects they are assigned to.
        
        projects = project.objects.filter(managerEmail=user.email)
        ongoing_count = projects.filter(status='O').count()
        completed_count = projects.filter(status='C').count()
        return render(request,'manager/manager_my_project.html',{'projects': projects, 'ongoing_count': ongoing_count, 'completed_count': completed_count})
        
    elif user.user_type == 'employee':
        projects = project.objects.filter(projectID__in=Task.objects.filter(employeeEmail=user.email).values_list('projectID', flat=True))
        return render(request,'employee/employee_view_project.html',{'projects': projects})

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

    return render(request, 'owner/edit_project.html', {'managers':managers,'project': project_instance})    


@login_required
def view_project_details(request,project_id):

    project_instance=project.objects.get(projectID=project_id)
    
    return render(request,'manager/manager_project_details.html',{'project_instance':project_instance})



#Project Manager
@login_required
def CreateTask(request,project_id):
    user = request.user
    
    project_instance = project.objects.get(projectID=project_id)
    owner_instance = owner.objects.get(email=project_instance.ownerEmail)
    employees = employee.objects.filter(company_name=owner_instance)

    
    if not user.user_type != manager:
        messages.error(request, "Only owners can edit projects.")
        return redirect('Logout')
    

    if request.method == 'POST':
        csrf_token = request.POST.get('csrfmiddlewaretoken')
        tasktitle = request.POST.get('task_title')
        description = request.POST.get('description')
        assignee = request.POST['employee'].split(' - ')
        deadline = request.POST.get('deadline')
        timestamp = datetime.now()
        
        task_instance = Task(
                taskID="TSK"+timestamp.strftime("%d%m%y%H%M%S"),
                taskTitle=tasktitle,
                description=description,
                deadline=deadline,
                assignedDate=timestamp,
                managerName=user.first_name,
                managerEmail=user.email,
                projectID=project_instance,
                employeeName = assignee[0],
                employeeEmail = assignee[1]
            )
        messages.success(request, 'Task Created Successfully.')
        task_instance.save()
        view_task_url = reverse('view-tasks', kwargs={'project_id': project_id})

        return redirect(view_task_url) 
    
    context = {'project_instance': project_instance,'employees' : employees}
    return render(request,'manager/create_task.html',context)



@login_required
def view_task_list(request,project_id):
    
    project_instance = project.objects.get(projectID=project_id) 
    task_instance=Task.objects.filter(projectID=project_instance)
    
    context = {'project_instance': project_instance,'task_instance':task_instance}
    return render(request, 'manager/manager_view_project.html', context)


@login_required
def view_task_details(request,project_id,task_id):
    
    user=request.user
    
    task_instance=Task.objects.get(taskID=task_id)
    project_instance = project.objects.get(projectID=project_id)
    
    context = {'project_instance': project_instance,'task_instance':task_instance}
    return render(request, 'manager/manager_view_task_details.html', context)
    

def edit_task(request, project_id, task_id):
    task_instance=Task.objects.get(taskID=task_id)
    user=request.user
    
    project_instance = project.objects.get(projectID=project_id)
    owner_instance = owner.objects.get(email=project_instance.ownerEmail)
    employees = employee.objects.filter(company_name=owner_instance)
    
    if user.user_type == employee:
        messages.error(request, "Only manager and owner can edit task")
        return redirect('Logout')
    
    if request.method == 'POST':
        
        task_instance.taskTitle = request.POST.get('task-title')
        task_instance.description = request.POST.get('description')
        task_instance.deadline = request.POST.get('deadline')
        assignee = request.POST['employee'].split('-')
        task_instance.employeeEmail=assignee[0]
        task_instance.employeeName=assignee[1]
        status=request.POST.get('status')
        
        if status == 'completed':
            task_instance.status='C'
            task_instance.completed=datetime.now()
        
        else:
            task_instance.status='I'
            task_instance.completed=None   
        
        task_instance.save()
        view_task_url = reverse('view-tasks', kwargs={'project_id': project_id}) 
        
        return redirect(view_task_url)
        
    return render(request, 'manager/edit_task.html', {'employees':employees,'project': project_instance,'task':task_instance})    
        
        
        
        
    

        
        

@login_required
def view_profile(request):
    return render(request,'profile.html')


