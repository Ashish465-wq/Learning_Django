from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact, Activity
from .forms import ContactForm, ActivityForm
from django.contrib.auth.decorators import login_required

@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'crm_app/contact_list.html', {'contacts': contacts})

@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    activity = Activity.objects.filter(contact=contact)
    return render(request, 'crm_app/contact_detail.html', {'contact': contact, 'activity': activity})

@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'crm_app/contact_form.html', {'form': form})

@login_required
def activity_create(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.contact = contact
            activity.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ActivityForm()
    return render(request, 'crm_app/activity_form.html', {'form': form, 'contact': contact})


