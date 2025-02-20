from django.urls import path
from report import views

app_name = 'report'

urlpatterns = [
    path('complaints-chart/', views.complaints_chart, name='complaints_chart'),
    path('api/get-complaints-data/', views.get_complaints_data, name='get_complaints_data'),
]
