from django.contrib.auth.models import Group
from userhandle.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from complaint.models import Complaint
from .forms import UserCreateForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from userhandle.decorators import allowed_users
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

@method_decorator(allowed_users(allowed_roles=['Admin', 'Staff']), name='dispatch')
class UserListView(ListView):
    model = CustomUser
    template_name = 'userhandle/user_list.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        # Exclude superusers from the queryset
        return CustomUser.objects.filter(is_superuser=False)

@allowed_users(allowed_roles=['Admin', 'Staff'])
@login_required
def user_create(request):
    if not request.user.is_superuser:
        return redirect('home:permission_denied')
    
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = False  # Ensure the user is not a superuser
            user.save()
            user.groups.add(form.cleaned_data['group'])  # Assign user to group
            messages.success(request, 'User created successfully!')
            return redirect(reverse_lazy('userhandle:users_list'))
    else:
        form = UserCreateForm()

    return render(request, 'userhandle/user_form.html', {'form': form})
    
@allowed_users(allowed_roles=['Admin', 'Staff'])    
@login_required
def user_update(request, user_id):
    if not request.user.is_superuser:
        return redirect('home:permission_denied')
    
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            updated_user = form.save(commit=False)
            updated_user.is_superuser = False  # Ensure the user is not a superuser
            updated_user.save()

            updated_user.groups.clear()
            updated_user.groups.add(form.cleaned_data['group'])

            messages.success(request, 'User updated successfully!')
            return redirect(reverse_lazy('userhandle:users_list'))
    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'userhandle/update_user.html', {'form': form})

@allowed_users(allowed_roles=['Admin', 'Staff'])
@login_required
def customer_complaints(request, pk):
    # Retrieve the customer by pk or raise 404 if not found
    customer = get_object_or_404(CustomUser, pk=pk)

    # Retrieve all complaints related to the customer
    complaints = Complaint.objects.filter(customer=customer)

    # Context to pass to the template
    context = {
        'complaints': complaints,
        'customer': customer,
    }

    # Render the template with the context
    return render(request, 'userhandle/customer_complaints.html', context)

