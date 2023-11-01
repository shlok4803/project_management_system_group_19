from django.shortcuts import render
from accounts.models import *

# Create your views here.
def dashboard(request):
    user = request.user 
    if isinstance(user,employee):
        return render(request,'dashboard_employee.html')
    
    elif isinstance(user,manager):
        return render(request,'dashboard_manager.html')
    
    elif isinstance(user,owner):
        return render(request,'dashboard_owner.html')
    
    
    
    
        
        
        