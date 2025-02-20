from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('no-permission/', views.permission_denied, name='permission_denied'),
    path('logs/', views.admin_logs, name='admin_logs'),
]
