from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')  
    
    lengh = int(request.GET.get('lengh', 12))
    if request.GET.get('uppercase'):
        characters += 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    if request.GET.get('special'):
        characters += '!@#$%^&*()'
    if request.GET.get('numbers'):
        characters += '1234567890'

    for x in range(lengh):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')