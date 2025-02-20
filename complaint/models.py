from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings

# Create your models here.
class Place(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Complaint(models.Model):
    
    PICK_POINT_CHOICES = (
        ('onsite', 'onsite'),
        ('offsite', 'offsite'),
    )
    
    CUSTOMER_TYPE_CHOICES = (
        ('person', 'person'),
        ('company', 'company'),
    )
    
    FINAL_STATUS_CHOICES = (
        ('return', 'return'),
        ('completed with issues', 'completed with issues'),
        ('completed', 'completed'),
        
    )
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer_complaints')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_remarks = models.TextField(blank=True, null=True, default=None)
    customer_type = models.CharField(max_length=10, choices=CUSTOMER_TYPE_CHOICES)
    complaint_description = models.TextField()
    home_address = models.CharField(max_length=100, blank=True, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    road = models.CharField(max_length=100, blank=True, null=True)
    landmark = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    pick_point = models.CharField(max_length=10, choices=PICK_POINT_CHOICES)
    appointment_date = models.DateTimeField()
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assigned_complaints', default=None, null=True, blank=True)
    out_sourced = models.BooleanField(default=False)
    out_sourced_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='outsourced_complaints', default=None, null=True, blank=True)
    out_sourced_expense = models.IntegerField(blank=True, null=True)
    total_expence = models.IntegerField(blank=True, null=True)
    final_status = models.CharField(max_length=30, choices=FINAL_STATUS_CHOICES, null=True, blank=True)
    bill_amount = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.customer.username} - {self.item.name}"