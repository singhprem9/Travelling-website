from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',index, name='home'),
    path('Kashmir',kwp, name='Kashmir'),
    path('Uk',UKS,name='uttrakhand'),
    path('about',about,name='about'),
    path('Contact',contact, name='Conatct'),
    path('agra',Agra, name='Agra'),
    path('delhi',Delhi,name='Delhi'),
    path('Mumbai',mumbai, name='Mumbai'),
    path('rajasthan',Raj, name='Rajasthan'),
    path('Ladakh',ladakh, name='Ladakh'),
    path('goa',goa, name='Goa'),
    path('hp',hp, name='Himachal Pradesh'),
    path('amritsar',amrit, name='Amritsar'),
    path('Kerala',keral, name='Kerala'),
    path('adventure',adv, name='Adventure'),
    path("Book",book, name='Book'),
    path("signup", signup, name='Sign-up'),
    path('login', login, name='login'),
    path('logout', signout, name='log-out'),
]
