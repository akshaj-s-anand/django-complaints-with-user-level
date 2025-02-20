from django.urls import path
from complaint import views
app_name = 'complaint'

urlpatterns = [
    path('', views.view_complaints, name='view_complaints'),
    path('add-complaint/', views.add_complaint, name= 'add_complaint'),
    path('update/<int:pk>/', views.update_and_delete_complaint, name='update_or_delete_complaint'),
    path('assigned-complaints/', views.assigned_complaints, name='assigned_complaints'),
    path('complaint-assigned-to-vendors/', views.complaint_assigned_to_vendors, name='complaint_assigned_to_vendors'),
    path('items/list/',views.list_item, name='list_item'),
    path('item/add/',views.add_item, name='add_item'),
    path('item/update/<int:pk>/', views.update_and_delete_item, name='update_and_delete_item'),
    path('place/list/',views.list_place, name='list_place'),
    path('place/add/', views.add_place, name='add_place'),
    path('place/update/<int:pk>/', views.update_and_delete_place, name='update_and_delete_place'),

]