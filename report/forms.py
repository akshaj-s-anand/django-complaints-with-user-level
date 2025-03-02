# forms.py

from django import forms
from complaint.models import Complaint, Item, Place
from django.contrib.auth import get_user_model

class ComplaintFilterForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=get_user_model().objects.all(), required=False)
    item = forms.ModelChoiceField(queryset=Item.objects.all(), required=False)
    customer_type = forms.ChoiceField(choices=Complaint.CUSTOMER_TYPE_CHOICES, required=False)
    place = forms.ModelChoiceField(queryset=Place.objects.all(), required=False)
    pick_point = forms.ChoiceField(choices=Complaint.PICK_POINT_CHOICES, required=False)
    final_status = forms.ChoiceField(choices=Complaint.FINAL_STATUS_CHOICES, required=False)
    assigned_to = forms.ModelChoiceField(queryset=get_user_model().objects.all(), required=False)
    out_sourced = forms.BooleanField(required=False)
