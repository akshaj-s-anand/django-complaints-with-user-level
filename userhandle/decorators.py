from django.http import HttpResponse
from django.shortcuts import redirect, render
from .middleware import PermissionDenied

def unauthenticated_user(view_func):
    def wraper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:login')
        else:
            return view_func(request, *args, **kwargs)
    return wraper_func


def allowed_users(allowed_roles= []):
    def decorator(view_func):
        def wraper_func(request, *args, **kwargs):
            
            group =None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                
            if group in allowed_roles:
                print('Working:', allowed_roles)
                return view_func(request, *args, **kwargs)
            elif request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home:permission_denied')
        return wraper_func
    return decorator