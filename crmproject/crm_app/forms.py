from django import forms
from .models import Contact, Activity

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'category', 'company', 'address']
        
class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['contact', 'activity_text']
        