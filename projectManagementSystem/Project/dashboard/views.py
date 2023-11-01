from django.shortcuts import render,redirect
from accounts.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from accounts.views import *

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
    
    
    
    
        
        
        