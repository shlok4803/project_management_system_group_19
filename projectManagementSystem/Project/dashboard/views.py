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
from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import os



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
        context={'projects': projects, 'ongoing_count': ongoing_count, 'completed_count': completed_count,'recent_projects':recent_projects}
        return render(request, 'owner/dashboard_owner.html', context)
    
    elif user.user_type == 'manager':
        # Redirect the manager to the manager dashboard
        projects = project.objects.filter(managerEmail=user.email)
        recent_projects = projects.order_by('-created')[:3]
        ongoing_count = projects.filter(status='O').count()
        completed_count = projects.filter(status='C').count()
        context={'projects': projects, 'ongoing_count': ongoing_count, 'completed_count': completed_count,'recent_projects':recent_projects}
        return render(request, 'manager/dashboard_manager.html', context)
    
    elif user.user_type == 'employee':
        # Redirect the employee to the employee dashboard
        task_instance = Task.objects.filter(employeeEmail=user.email)
        recent_task = task_instance.order_by('-assignedDate')[:3]
        ongoing_count = task_instance.filter(status='I').count()
        completed_count = task_instance.filter(status='C').count()
        context={'projects': projects, 'ongoing_count': ongoing_count, 'completed_count': completed_count,'recent_tasks':recent_task}
        return render(request,'employee/dashboard_employee.html',context)

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
    context={'managers':managers}
    return render(request, 'owner/create_project.html',context)

#Owner,PM,Employee
@login_required
def view_project(request):
    user = request.user
    projects = None
    
    if user.user_type == 'owner': 
        # Owners can view all projects.
        
        projects = project.objects.all() 
        context={'projects': projects}
        return render(request,'owner/owner_view_project.html',context)
        
    elif user.user_type == 'manager': 
        # Managers can view projects they are assigned to.
        
        projects = project.objects.filter(managerEmail=user.email)
        ongoing_count = projects.filter(status='O').count()
        completed_count = projects.filter(status='C').count()
        context={'projects': projects, 'ongoing_count': ongoing_count, 'completed_count': completed_count}
        return render(request,'manager/manager_my_project.html',context)
        
    elif user.user_type == 'employee':
        projects = project.objects.filter(projectID__in=Task.objects.filter(employeeEmail=user.email).values_list('projectID', flat=True))
        context={'projects': projects}
        
        return render(request,'employee/employee_my_project.html',context)

#Owner   
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

#Owner,PM,Employee
@login_required
def view_project_details(request,project_id):

    project_instance=project.objects.get(projectID=project_id)
    user=request.user
    if user.user_type =='owner':
        return render(request,'owner/owner_view_project_details.html',{'project_instance':project_instance})
    
    elif user.user_type in ('manager' ,'employee'):
        return render(request,'manager/manager_project_details.html',{'project_instance':project_instance})

#Owner    
@login_required    
def complete_project(request, project_id):
    project_instance=project.objects.get(projectID=project_id)
    task_instance = Task.objects.filter(projectID=project_instance)

    # Check if all tasks are completed
    all_tasks_completed = all(task.status == 'C' for task in task_instance)

    if all_tasks_completed:
        # Update the project completion date
        project_instance.completed = datetime.now()
        project_instance.status = 'C'  # Update project status to 'Completed'
        project_instance.save()
        return JsonResponse({'message': 'Project completed successfully'})
        

    return JsonResponse({'message': 'Tasks are pending'})  

@login_required    
def viewChat(request,project_id):
    curProject=project.objects.get(projectID=project_id)
    # curTasks = Task.objects.filter(projectID=project_id)
    # curEmployees = employee.objects.filter(taskID__in=curTasks)
    user=request.user
    curRole='N'
    if owner.objects.filter(email=curProject.ownerEmail).filter(email=user.email):
        curRole='O'
    elif manager.objects.filter(email=curProject.managerEmail).filter(email=user.email):
        curRole='M'
    elif Task.objects.filter(employeeEmail=user.email).filter(projectID=project_id):
        curRole='E'
    else:
        messages.error(request, "You don't have access to this page")
        return redirect('/dashboard')
    
    if request.method == 'POST':
        csrf_token = request.POST.get('csrfmiddlewaretoken')
        newText = request.POST.get('Text')
        timestamp = datetime.now()
        newChatID="CHT"+timestamp.strftime("%d%m%y%H%M%S")
        
        newMessage = message(
            chatID=newChatID,
            prevMessage=curProject.chat,
            text=newText,
            senderName=user.first_name,
            senderEmail=user.email,
            role=curRole
        )
        project.objects.filter(projectID=curProject.projectID).update(chat=newChatID)
        newMessage.save()
        
        return redirect('/dashboard/project/chat/'+curProject.projectID)

    allMessage=[]
    curChatID=curProject.chat
    while curChatID!='NULL':
        allMessage.append(message.objects.get(chatID=curChatID))
        curChatID=message.objects.get(chatID=curChatID).prevMessage
    allMessage.reverse()

    return render(request, 'view_chats.html', {'project':curProject,'messages': allMessage})
    
#Owner   
@login_required        
def delete_project(request,project_id):
    print(project_id)
    try:
        project_instance = project.objects.get(projectID=project_id)
        project_instance.delete()
        return redirect('/dashboard/project/')
        
    except project.DoesNotExist:
        return redirect('')
        return JsonResponse({'error': 'Project does not exist'}, status=404)
    
    
#Owner
@login_required
def manage_employee(request):
    
    manager_instance=manager.objects.all()
    employee_instance=employee.objects.all()
    
    context={'manager_instance':manager_instance,'employee_instance':employee_instance}
    
    return render(request,'owner/owner_manage_employee.html',context)    






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


#Owner,PM,Employee
@login_required
def view_task_list(request,project_id):
    
    user=request.user
    
    project_instance = project.objects.get(projectID=project_id) 
    task_instance=Task.objects.filter(projectID=project_instance)
    
    context = {'project_instance': project_instance,'task_instance':task_instance}
    
    if user.user_type == 'owner':
        return render(request,'owner/owner_view_task_list.html',context)
    
    elif user.user_type == 'manager':
        return render(request, 'manager/manager_view_task_list.html', context)
    
    elif user.user_type == 'employee':
        
        task_instance=Task.objects.filter(employeeEmail=user.email)
        return render(request,'employee/employee_view_task_list.html',context)


#PM,Employee
@login_required
def view_task_details(request,project_id,task_id):
    
    user=request.user
    task_instance=Task.objects.get(taskID=task_id)
    project_instance = project.objects.get(projectID=project_id)
    context = {'project_instance': project_instance,'task_instance':task_instance}
    
    if user.user_type == 'manager':
        return render(request, 'manager/manager_view_task_details.html', context)
    
    elif user.user_type == 'employee':
        return render(request,'employee/employee_view_task_details.html',context)

#Employee
@login_required
def submit_task(request,task_id):
    task_instance=Task.objects.get(taskID=task_id)
    task_instance.submitted=datetime.now()
    
    if task_instance.submitted > task_instance.deadline:
        task_instance.late = True
        
    
#PM    
@login_required
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
        task_instance.employeeName=assignee[0]
        task_instance.employeeEmail=assignee[1]
        status=request.POST.get('taskstatus')
        
        if status == 'C':
            task_instance.status='C'
            task_instance.completed=datetime.now()
        
        elif status == 'I':
            task_instance.status='I'
            task_instance.completed=None
               
        
        task_instance.save()
        view_task_detail = reverse('view-taskdetail', kwargs={'project_id': project_id,'task_id':task_id}) 
        
        return redirect(view_task_detail)
        
    return render(request, 'manager/edit_task.html', {'employees':employees,'project_instance': project_instance,'task_instance':task_instance})    

#PM    
@login_required        
def delete_task(request,task_id,project_id):
    #project_instance=project.objects.get(projectID=project_id)
    try:
        task = Task.objects.get(taskID=task_id)
        task.delete()
        view_tasks_url = reverse('view-tasks', kwargs={'project_id': project_id})
        return redirect(view_tasks_url)
        
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task does not exist'}, status=404)
          

#Owner,PM,Employee
@login_required
def view_profile(request):
    user = request.user

    company_name = None  # Default value if company name is not found
    context = {
        'user': user,
        'company_name': company_name,
    }


    # Retrieve company name based on the user's type
    
    if user.user_type == 'owner':
            owner_user = owner.objects.get(email=user.email)
            company_name = owner_user.company_name
            return render(request, 'owner/owner_profile_page.html', context)
    elif user.user_type == 'manager':
            manager_user = manager.objects.get(email=user.email)
            company_name = manager_user.company_name.company_name
            return render(request, 'manager/manager_profile_page.html', context)
            
    elif user.user_type == 'employee':
            employee_user = employee.objects.get(email=user.email)
            company_name = employee_user.company_name.company_name
            return render(request, 'employee/employee_profile_page.html', context)
            
       

   
   


#Owner,PM,Employee
@login_required
def update_profile(request):
    if request.method == 'POST' and request.is_ajax():
        user = request.user
        if user.is_authenticated:
            try:
                user.first_name = request.POST.get('fullname')
                user.contact = request.POST.get('contact')
                user.role = request.POST.get('role')
                user.company = request.POST.get('company')
                user.save()
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request'})
    

#Owner,PM    
def view_progress(request, project_id):
    project_instance = project.objects.get(projectID=project_id)
    task_instance = Task.objects.filter(projectID=project_instance)
    
    total_task = task_instance.count()  # Total tasks for the project
    
    in_progress_tasks = task_instance.filter(status='I').count()
    completed_tasks = task_instance.filter(status='C').count()
    review_tasks = task_instance.filter(status='R').count()
    
    # Calculate total completed tasks considering all tasks in 'C' and 'R' status
    total_completed = completed_tasks + review_tasks + in_progress_tasks
    
    # Calculate progress percentage
    if total_task > 0:
        progress_percentage = (total_completed / total_task) * 100
    else:
        progress_percentage = 0
    
    context = {
        'progress': progress_percentage,
        'project_instance': project_instance
    }
    
    return render(request, 'progress_page.html', context)



