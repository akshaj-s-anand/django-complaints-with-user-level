from django.shortcuts import render, redirect
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.admin.models import LogEntry
from userhandle.decorators import allowed_users   
from complaint.models import Complaint
from report.views import users as Users

# Create your views here.


@login_required
@allowed_users(allowed_roles=['Admin', 'Staff'])
def home(request):
    complaints = Complaint.objects.order_by('-id')[:10]
    users = Users.objects.order_by('-id')[:10]
    weather_info = get_weather()
    
    context= {
        "complaints":complaints,
        'weather_info':weather_info,
        'home_active':True,
        'users':users
        
    }
    return render(request, 'home/home.html', context)

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


#widgets area
def get_weather():
    api_key = "b04d43352f3e7954ac6ac4f99d87d4ba"

    # Get real public IP
    ip_response = requests.get("https://api64.ipify.org?format=json")
    ip = ip_response.json().get("ip", "")

    # Get geolocation from the real public IP
    geo_url = f"http://ip-api.com/json/{ip}"
    geo_response = requests.get(geo_url).json()

    if geo_response["status"] != "success":
        return {"error": "Could not determine location"}

    lat, lon = geo_response["lat"], geo_response["lon"]

    # Call OpenWeather API
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    weather_response = requests.get(weather_url).json()

    if "main" not in weather_response:
        return {"error": "Failed to fetch weather data"}

    # Extract weather data
    weather_info = {
        "temperature": weather_response["main"]["temp"],
        "humidity": weather_response["main"]["humidity"],
        "wind_speed": weather_response["wind"]["speed"],
        "description": weather_response["weather"][0]["description"],
        "location": weather_response["name"],
        "latitude": lat,
        "longitude": lon,
    }

    return weather_info