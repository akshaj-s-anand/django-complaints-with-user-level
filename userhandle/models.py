from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class ServiceType(models.Model):
    name = models.CharField(max_length=128)


class CustomUser(AbstractUser):
    service_center_address = models.CharField(max_length=128, blank=True, null=True)
    service_center_location = models.CharField(max_length=128, blank=True, null=True)
    service_center_phone_number_1 = models.CharField(max_length=15, blank=True, null=True)
    service_center_phone_number_2 = models.CharField(max_length=15, blank=True, null=True)
    service_type = models.ForeignKey('ServiceType', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'auth_user'