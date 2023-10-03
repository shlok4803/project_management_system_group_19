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
        return redirect("/home")
    return render(request, 'register.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/home")

    context = {}
    if request.method == 'POST':
        email = request.POST["email_user"]
        password = request.POST["password"]

        username = CustomUser.objects.filter(email=email.lower()).first()
        
        if username is None:
            context = {"error": "User not found, Register your account first."}
            return render(request, 'login.html', context)
        
        if username.is_active==False:
            context = {"error": "Please verify your email address first."}
            return render(request, 'login.html', context)
        
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            context = {"error": "Invalid password"}
            return render(request, 'login.html', context)
        
        
        login(request,user)
        msg = "Welcome " + CustomUser.objects.get(email=email).first_name + " !!"
        messages.success(request,msg)
        return redirect("/home")

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
            send_verification_email(request, form)
            messages.success(request, 'Please verify your email for ProPlaning and login after that')
            return redirect('/login')
    return render(request, 'register_owner.html', {"form": form})


def register_view_manager(request):
    if request.user.is_authenticated:
        return redirect("/home")
    form = SignupForm_manager()
    if request.method == 'POST':
        form = SignupForm_manager(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Please verify your email for ProPlaning and login after that')
            return redirect('/login')
    return render(request, 'register_manager.html', {"form": form})


def register_view_employee(request):
    if request.user.is_authenticated:
        return redirect("/home")
    form = SignupForm_employee()
    if request.method == 'POST':
        form = SignupForm_employee(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Please verify your email for ProPlaning and login after that')
            return redirect('/login')
    return render(request, 'register_employee.html', {"form": form})



@login_required
def home_view(request):
    return render(request, 'home.html')