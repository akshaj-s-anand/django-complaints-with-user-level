from django import forms
from django.contrib.auth.models import Group
from userhandle.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserCreateForm(UserCreationForm):
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'group', 'first_name', 'email', 'password1', 'password2', 'service_center_address', 'service_center_location', 'service_center_phone_number_1', 'service_center_phone_number_2', 'service_type']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'service_center_address': forms.TextInput(attrs={'class': 'form-control'}),
            'service_center_location': forms.TextInput(attrs={'class': 'form-control'}),
            'service_center_phone_number_1': forms.TextInput(attrs={'class': 'form-control'}),
            'service_center_phone_number_2': forms.TextInput(attrs={'class': 'form-control'}),
            'service_type': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("A user with that username already exists.")
        return username

class UserUpdateForm(UserChangeForm):
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser  # Use custom user model
        fields = ['username', 'group', 'first_name', 'email', 
                  'service_center_address', 'service_center_location', 
                  'service_center_phone_number_1', 'service_center_phone_number_2', 
                  'service_type']  # No password field
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'service_center_address': forms.TextInput(attrs={'class': 'form-control'}),
            'service_center_location': forms.TextInput(attrs={'class': 'form-control'}),
            'service_center_phone_number_1': forms.TextInput(attrs={'class': 'form-control'}),
            'service_center_phone_number_2': forms.TextInput(attrs={'class': 'form-control'}),
            'service_type': forms.Select(attrs={'class': 'form-control'}),
        }