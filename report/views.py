from django.shortcuts import render
from django.http import JsonResponse
from complaint.models import Complaint
import datetime
from django.db.models import Sum, Count, Q
from userhandle.decorators import allowed_users

@allowed_users(allowed_roles=['Admin'])
def complaints_chart(request):
    """ Renders the template with the chart """
    return render(request, 'report/complaints_chart.html')


@allowed_users(allowed_roles=['Admin'])
def get_complaints_data(request):
    """ API to fetch complaints data based on a date range """

    start_date = request.GET.get('appointment_date')
    end_date = request.GET.get('end_date')

    # If no date range is provided, use the last 7 days by default
    if not start_date or not end_date:
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=7)

    complaints = Complaint.objects.filter(appointment_date__range=[start_date, end_date])

    # Group by date
    data = complaints.values('appointment_date').annotate(
        total_complaints=Count('id'),
        outsourced_complaints=Count('id', filter=Q(out_sourced=True)),
        total_bill=Sum('bill_amount', default=0)
    ).order_by('appointment_date')

    return JsonResponse(list(data), safe=False)
