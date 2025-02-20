from django.urls import path
from .views import UserListView, user_create, user_update
from . import views
app_name = 'userhandle'

urlpatterns = [
    path('list/', UserListView.as_view(), name='users_list'),
    path('create/', user_create, name='user_create'),
    path('user/update/<int:user_id>/', user_update, name='user_update'),
     path('complaints/<int:pk>/', views.customer_complaints, name='customer_complaints'),
]
