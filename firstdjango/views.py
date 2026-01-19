from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'homepage/index.html')

def contactus(request):
    return render(request, 'contactus/index.html')