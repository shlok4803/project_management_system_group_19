from django.shortcuts import render
from accounts.models import *
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime

# Create your views here.
def dashboard(request):
    user = request.user 
    if isinstance(user,employee):
        return render(request,'dashboard_employee.html')
    
    elif isinstance(user,manager):
        return render(request,'dashboard_manager.html')
    
    elif isinstance(user,owner):
        return render(request,'dashboard_owner.html')
    
    
    
    
        
        
        

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
