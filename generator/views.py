from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'huiauhe3'}) #render brukes når man skal hent side fra template. mappe/fil 

def password(request):
    
    characters = list('asbcdefghijklmnopqrstuvwxyzæøå')
    
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ')
    
    if request.GET.get('numbers'):
        characters.extend('123456789')
  
    if request.GET.get('special'):
        characters.extend('?=)(/&%¤#"!)')        
            
    length = int(request.GET.get('length',12))
    
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password':thepassword}) #render brukes når man skal hent side fra template. mappe/fil 

def about(request):
    
    return render(request, 'generator/about.html')