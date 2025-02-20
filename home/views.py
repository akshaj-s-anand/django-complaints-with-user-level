from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.admin.models import LogEntry
from userhandle.decorators import unauthenticated_user, allowed_users   
# Create your views here.

@login_required
@allowed_users(allowed_roles=['Admin', 'Staff'])
def home(request):
    return render(request, 'home/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home/home.html')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'home/login.html')
            
    return render(request, 'home/login.html')

def logout_view(request):
    logout(request)
    return redirect('home:login')

@login_required
def permission_denied(request):
    return render(request, "home/permission_denied.html")

@allowed_users(allowed_roles=['Admin'])
@login_required
def admin_logs(request):  
    logs = LogEntry.objects.select_related('user', 'content_type').order_by('-action_time')
    return render(request, 'home/admin_logs.html', {'logs': logs})


