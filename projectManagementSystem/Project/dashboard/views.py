from django.shortcuts import render,redirect
from accounts.models import *
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from accounts.views import *
from .models import *
from datetime import datetime
# Owner, PM and Employee
@login_required
def dashboard(request):
    
    if request.user.is_staff:
        messages.error(request, "Staff accounts cannot be used.")
        return redirect('Logout')
    
    if not request.session.get('employee'):
        messages.error(request, "Session logged out due to inactivity.")
        return redirect('Logout')
    
    user = request.user 
    if isinstance(user,employee):
        return render(request,'dashboard_employee.html')
    
    elif isinstance(user,manager):
        return render(request,'dashboard_manager.html')
    
    elif isinstance(user,owner):
        return render(request,'dashboard_owner.html')
    
    elif  user != 'employee' and user !='manager' and user != 'owner':
        raise PermissionDenied
    
    
    
    
        
        
        

# @login_required
def CreateProject(request):
    user=request.user

    # If use do not have access to create project
    if not user.is_authenticated:
        return redirect('Logout')
    if isinstance(user,employee):
        messages.error(request, "Employee Can't Create Project")
        return redirect('Logout')
    if isinstance(user,manager):
        messages.error(request, "Manager Can't Create Project")
        return redirect('Logout')
    
    if request.method == "POST":
        timestamp = datetime.now()
        project = Project(
            projectID="PRJ"+timestamp.strftime("%d%m%y%H%M%S"),
            title=request.POST['title'],
            description=request.POST['description'],
            deadline=request.POST['deadline'],
            managerEmail=request.POST['managerEmail'],
            managerName=request.POST['managerName'],
            status='O'
        )
        project.save()
        messages.success(request, 'Project Created Successfully.')
        return redirect('ViewProjects')
    return render(request, 'createProject', {})
