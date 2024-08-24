from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact, Activity
from .forms import ContactForm, ActivityForm


def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'crm_app/contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    activity = Activity.objects.filter(contact=contact)
    return render(request, 'crm_app/contact_detail.html', {'contact': contact, 'activity': activity})


