from django.urls import path
from report import views

app_name = 'report'

urlpatterns = [
    path('complaints-chart/', views.complaint_filter_view, name='complaints_chart'),
]
