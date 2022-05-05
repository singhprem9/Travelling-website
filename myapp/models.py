import numbers
from unicodedata import numeric
from django.db import models


# Create your models here.
class Travels(models.Model):
    name=models.CharField(max_length=50)
    Place=models.CharField(max_length=50)
    description=models.CharField(max_length=400,default='')
    image=models.ImageField(upload_to='uploads/Tours/')
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_travels():
        return Travels.objects.all()
    
class Safari(models.Model):
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=450)
    image=models.ImageField(upload_to='uploads/Tours/')
    
    def __str__(self):
        return self.Name
    
        
class Contact(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Emailid=models.EmailField(max_length=35)
    Message=models.CharField(max_length=250)
    
    def __str__(self):
        return  self.Firstname
    
    def records(self):
        self.save()
    

class Booking(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    booking_date=models.DateField()
    other_messages=models.CharField(max_length=300)
    
    def __str__(self):
        return self.first_name
    
    def register(self):
        self.save() 
        
