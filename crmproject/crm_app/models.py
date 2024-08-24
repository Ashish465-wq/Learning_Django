from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    category = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    address = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Activity(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    activity_text = models.TextField()
    
    def __str__(self):
        return f"Activity for {self.contact.first_name} on {self.date}"
    
       
