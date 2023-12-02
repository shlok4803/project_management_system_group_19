from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import SignupForm_employee,SignupForm_owner,SignupForm_manager
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from verify_email.email_handler import send_verification_email


# Create your views here.
def landing_view(request):
    if request.user.is_authenticated:
        return redirect("/dashboard")
    return render(request, 'landing.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/dashboard")

    context = {}
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]

        user = CustomUser.objects.filter(email=email.lower()).first()

        if user is None:
            context = {"error": "User not found, Register your account first."}
            return render(request, 'login.html', context)
        
        if user.is_active==False:
            context = {"error": "Please verify your email address first."}
            return render(request, 'login.html', context)
        
        authUser = authenticate(request, email=email, password=password)
        
        if authUser is None:
            context = {"error": "Invalid password"}
            return render(request, 'login.html', context)
        
        
        login(request,authUser)
        msg = "Welcome " + CustomUser.objects.get(email=email).first_name + " !!"
        messages.success(request,msg)
        return redirect("/dashboard")

    return render(request, "login.html", context)



def register_view(request):
    if request.user.is_authenticated:
        return redirect("/home")
    return render(request, "register.html")



def register_view_owner(request):
    if request.user.is_authenticated:
        return redirect("/home")
    form = SignupForm_owner()
    if request.method == 'POST':
        form = SignupForm_owner(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_type = 'owner'
            user.save()
            send_verification_email(request, form)
            messages.success(request, 'Please verify your email for ProPlaning and login after that')
            return redirect('/login')
    return render(request, 'owner/register_as_admin.html', {"form": form})


def register_view_manager(request):
    if request.user.is_authenticated:
        return redirect("/home")
    form = SignupForm_manager()
    if request.method == 'POST':
        form = SignupForm_manager(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_type = 'manager'
            user.save()
            send_verification_email(request, form)
            messages.success(request, 'Please verify your email for ProPlaning and login after that')
            return redirect('/login')
    return render(request, 'manager/register_as_manager.html', {"form": form})


def register_view_employee(request):
    if request.user.is_authenticated:
        return redirect("/home")
    form = SignupForm_employee()
    if request.method == 'POST':
        form = SignupForm_employee(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_type = 'employee'
            user.save()
            send_verification_email(request, form)
            messages.success(request, 'Please verify your email for ProPlaning and login after that')
            CustomUser.is_employee=True
            return redirect('/login')
    return render(request, 'employee/register_as_employee.html', {"form": form})

def Logout(request):
    request.session.flush()
    logout(request)
    return redirect('')



@login_required
def home_view(request):
    return render(request, 'home.html')