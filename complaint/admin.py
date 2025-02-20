from django.contrib import admin
from complaint.models import Place, Item, Complaint
# Register your models here.


admin.site.register(Place)
admin.site.register(Item)
admin.site.register(Complaint)
