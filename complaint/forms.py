from complaint.models import Complaint, Item, Place
from django.forms import ModelForm
from django.contrib.auth.models import Group
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = "__all__"

        labels = {
            'customer': 'Customer Name',
            'item': 'Item',
            'item_remarks': 'Item Remarks',
            'customer_type': 'Customer Type',
            'complaint_description': 'Complaint Description',
            'home_address': 'Home Address',
            'place': 'Place',
            'road': 'Road',
            'landmark': 'Landmark',
            'phone_number': 'Phone Number',
            'pick_point': 'Pick-up Point',
            'appointment_date': 'Appointment Date & Time',
            'assigned_to': 'Assigned To',
            'out_sourced': 'Outsourced',
            'out_sourced_to': 'Outsourced To',
            'out_sourced_expense': 'Outsourcing Expense',
            'total_expence': 'Total Expense',
            'final_status': 'Final Status',
            'bill_amount': 'Bill Amount',
        }

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select a Customer'}),
            'item': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select an Item'}),
            'item_remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter item remarks', 'rows': 3}),
            'customer_type': forms.Select(attrs={'class': 'form-control'}),
            'complaint_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe the complaint', 'rows': 4}),
            'home_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter home address'}),
            'place': forms.Select(attrs={'class': 'form-control'}),
            'road': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter road name'}),
            'landmark': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter nearby landmark'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'pick_point': forms.Select(attrs={'class': 'form-control'}),
            'appointment_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type':'datetime-local', 'placeholder': 'Select appointment date & time'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
            'out_sourced': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'id_out_sourced'}),
            'out_sourced_to': forms.Select(attrs={'class': 'form-control', 'id': 'id_out_sourced_to'}),
            'out_sourced_expense': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_out_sourced_expense', 'placeholder': 'Enter outsourcing expense'}),
            'total_expence': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter total expense'}),
            'final_status': forms.Select(attrs={'class': 'form-control'}),
            'bill_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter bill amount'}),
        }

    # ✅ Correct Filtering for customer, assigned_to, and out_sourced_to
    def __init__(self, *args, **kwargs):
        super(ComplaintForm, self).__init__(*args, **kwargs)

        # Function to safely get a group and return filtered users
        def get_users_by_group(group_id):
            try:
                group = Group.objects.get(id=group_id)
                return User.objects.filter(groups=group)
            except Group.DoesNotExist:
                return User.objects.none()

        # Load users based on group IDs
        self.fields['customer'].queryset = get_users_by_group(3)  # Group ID 3
        self.fields['assigned_to'].queryset = get_users_by_group(2)  # Group ID 2
        self.fields['out_sourced_to'].queryset = get_users_by_group(4)  # Group ID 4

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        
        labels = {
            'name':'Item name',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name'}),
        }
        
class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = "__all__"
        
        labels = {
            'name':'Place',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter place name'}),
        }
        
