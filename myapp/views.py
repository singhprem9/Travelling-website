from cmath import log
from multiprocessing import context
from django import http
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser, logout
from myapp.forms import RegistrationForm, LoginForm


from MagicSafari.settings import STATIC_URL
from .models import Booking, Contact, Travels, Safari
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def index(request):
    travels=Travels.get_all_travels();
    print(travels[0].image)
    return render(request,'home.html',{'travels': travels,'STATIC_URL':STATIC_URL})

def Agra(request):
    return render(request,'agra.html')

def Delhi(request):
    return render(request,'delhi.html')

def mumbai(request):
    return render(request,'Mumbai.html')

def Raj(request):
    return render(request,'Rajasthan.html')

def goa(request):
    return render(request,'Goa.html')

def ladakh(request):
    return render(request,'Ladakh.html')

def kwp(request):
    return render(request, 'Kashmir.html')

def UKS(request):
    return render(request,'Uk.html')

def hp(request):
    return render(request,'Hp.html')

def amrit(request):
    return render(request,'Amritsar.html')

def keral(request):
    return render(request,'Kerala.html')

def about(request):
    return render(request,'about us.html')

def contact(request):
    n=""
    if request.method=="POST":
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        message=request.POST.get('message')
        print(first_name,last_name,email,message)
        contact=Contact(Firstname=first_name,Lastname=last_name,Emailid=email,Message=message)
        contact.records() 
        n='Your details has been sent!'
    return render(request,'Contact.html',{'n':n})
        


def adv(request):
    return render(request,'adventure.html')

def book(request):
    n=""
    if request.method=="POST": 
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        booking_date=request.POST.get('bookingdate')
        other_message=request.POST.get('othermessage')
        print(first_name,last_name,phone,email,booking_date,other_message)
        booking=Booking(first_name=first_name,last_name=last_name,phone=phone,email=email,booking_date=booking_date, other_messages=other_message)
        booking.save()
        n='Congarts! Your Booking is Successfull!!'
    return render(request,'Book.html',{'n':n})

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        context={
            "form" : form
        }
        return render(request, 'login.html', context=context)
    else:
        form = LoginForm(request=request, data=request.POST)
        print(form.is_valid())
        if form.is_valid():
                return redirect('/')
        else:
            context= {
                'form' : form
            }
        return render(request, 'login.html', context=context)
        

def signup(request):
    if request.method == "GET":
        form =RegistrationForm()
        context = {
            "form" : form
        }
        return render(request, 'signup.html', context=context)
    else:
        form = RegistrationForm(request.POST)
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('/login')
        else:
            return render(request, 'signup.html', context=context)

def signout(request):
    logout(request)
    return redirect('/')
    

