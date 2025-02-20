from django.shortcuts import render, redirect
from complaint.models import Complaint, Group, Item, Place
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from complaint.forms import ComplaintForm, ItemForm, PlaceForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from userhandle.decorators import allowed_users
# Create your views here.


@login_required
@allowed_users(allowed_roles=['Admin', 'Staff'])
def view_complaints(request):
    
    complaints = Complaint.objects.all()
    
    context = {
        
        'complaints':complaints,
               
        }
    
    
    return render(request, 'complaint/view_complaints.html', context)


@login_required
@allowed_users(allowed_roles=['Admin'])
def add_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.save()
            messages.success(request, 'Complaint added successfully!')
            return redirect(reverse('complaint:view_complaints'))  # Redirect instead of render

    else:
        form = ComplaintForm()

    context = {'form': form}
    return render(request, 'complaint/add_and_update_complaint.html', context)

@login_required
@allowed_users(allowed_roles=['Admin', 'Staff'])
def update_and_delete_complaint(request, pk):
    complaint = get_object_or_404(Complaint, id=pk)

    # Deleting complaint
    if request.method == 'POST' and "delete" in request.POST:
        complaint.delete()
        messages.success(request, 'Complaint deleted successfully!')
        return redirect('complaint:view_complaints')

    # Updating complaint
    form = ComplaintForm(request.POST or None, instance=complaint)
    if form.is_valid():
        form.save()
        messages.success(request, 'Complaint Updated successfully!')
        return redirect('complaint:view_complaints')

    context = {
        'form': form,
        'complaint': complaint,
        'delete_button': True,
    }

    return render(request, 'complaint/add_and_update_complaint.html', context)

@login_required
@allowed_users(allowed_roles=['Admin', 'Staff'])
def assigned_complaints(request):
    complaints = Complaint.objects.filter(assigned_to=request.user)  # Filter assigned complaints
    return render(request, 'complaint/my_complaints.html', {'complaints': complaints})


@login_required
@allowed_users(allowed_roles=['Admin', 'Staff'])
def complaint_assigned_to_vendors(request):
    complaints = Complaint.objects.filter(out_sourced_to__isnull=False)
    return render(request, 'complaint/complaint_assigned_to_vendors.html', {'complaints': complaints})


@login_required
@allowed_users(allowed_roles=['Admin', 'Staff'])
def list_item(request):
    items = Item.objects.all()
    
    context = {
        'items':items, 
    }
    return render(request, 'complaint/list_item.html', context)

@login_required
@allowed_users(allowed_roles=['Admin', 'Staff'])
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            items = form.save(commit=False)
            items.save()
            messages.success(request, 'Item created successfully!')
            return redirect(reverse('complaint:list_item'))  # Redirect instead of render

    else:
        form = ItemForm()

    context = {'form': form}
    return render(request, 'complaint/add_and_update_item.html', context)

@login_required
@allowed_users(allowed_roles=['Admin', 'Staff'])
def update_and_delete_item(request, pk):
    items = get_object_or_404(Item, id=pk)

    # Deleting item
    if request.method == 'POST' and "delete" in request.POST:
        items.delete()
        messages.success(request, 'Item deleted successfully!')
        return redirect('complaint:list_item')

    # Updating item
    form = ItemForm(request.POST or None, instance=items)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Item updated successfully!')
        return redirect('complaint:list_item')
    elif request.method == 'POST':
        messages.error(request, 'Failed to update the item!')

    context = {
        'form': form,
        'items': items,
        'delete_button': True,
    }

    return render(request, 'complaint/add_and_update_item.html', context)

@login_required
@allowed_users(allowed_roles=['Admin', 'Staff'])
def list_place(request):
    place = Place.objects.all()
    
    context = {
        'place':place, 
    }
    return render(request, 'complaint/list_place.html', context)

@login_required
@allowed_users(allowed_roles=['Admin', 'Staff'])
def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            place = form.save(commit=False)
            place.save()
            messages.success(request, 'Place created successfully!')
            return redirect(reverse('complaint:list_place'))  # Adjusted for places

    else:
        form = PlaceForm()

    context = {'form': form}
    return render(request, 'complaint/add_and_update_place.html', context)  # Updated template name

@login_required
@allowed_users(allowed_roles=['Admin', 'Staff'])
def update_and_delete_place(request, pk):
    place = get_object_or_404(Place, id=pk)

    # Deleting place
    if request.method == 'POST' and "delete" in request.POST:
        place.delete()
        messages.success(request, 'Place deleted successfully!')
        return redirect('complaint:list_place')

    # Updating place
    form = PlaceForm(request.POST or None, instance=place)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Place updated successfully!')
        return redirect('complaint:list_place')
    elif request.method == 'POST':
        messages.error(request, 'Failed to update the place!')

    context = {
        'form': form,
        'place': place,
        'delete_button': True,
    }

    return render(request, 'complaint/add_and_update_place.html', context)

