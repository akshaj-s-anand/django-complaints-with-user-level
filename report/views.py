from django.shortcuts import render
from complaint.models import Complaint
from complaint.models import Complaint
from userhandle.decorators import allowed_users
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils import timezone
from datetime import timedelta

users = get_user_model()


@allowed_users(allowed_roles=['Admin'])
def complaint_filter_view(request):
    
    now = timezone.now()
    thiry_days_ago = now - timedelta(days=30)
    
    # Start with all complaints
    total_complaints = Complaint.objects.count()
    total_users = users.objects.count()
    staff_group = Group.objects.get(name='Staff')
    admin_group = Group.objects.get(name='Admin')
    customer_group = Group.objects.get(name='Customer')
    service_center_group = Group.objects.get(name='Service Center')
    total_staffs = staff_group.user_set.count()
    total_admin = admin_group.user_set.count()
    total_customers = customer_group.user_set.count()
    total_service_centers = service_center_group.user_set.count()
    
    new_users = users.objects.filter(date_joined__gte = thiry_days_ago).count()
    new_complaints = Complaint.objects.filter(appointment_date__gte = thiry_days_ago).count()
    
    complaints_with_service_centers_status_none = Complaint.objects.filter(out_sourced=True, final_status__isnull = True).count()
    complaints_with_status_none = Complaint.objects.filter(final_status__isnull = True).count()
    return_complaints = Complaint.objects.filter(final_status = 'return').count()
    completed_with_issues = Complaint.objects.filter(final_status = 'completed with issues').count()
    completed_complaints = Complaint.objects.filter(final_status = 'completed').count()

    # Render the page with the form and complaints
    context = {
        'total_complaints': total_complaints,
        'total_users':total_users,
        'total_staffs':total_staffs,
        'total_admin':total_admin,
        'total_customers':total_customers,
        'total_service_centers':total_service_centers,
        
        'new_users':new_users,
        'new_complaints':new_complaints,
        
        'complaints_with_service_centers_status_none':complaints_with_service_centers_status_none,
        'complaints_with_status_none':complaints_with_status_none,
        'return_complaints':return_complaints,
        'completed_with_issues':completed_with_issues,
        'completed_complaints':completed_complaints,
        
    }
    return render(request, 'report/report.html', context)
