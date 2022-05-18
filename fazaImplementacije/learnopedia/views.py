from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest

def index(request: HttpRequest):
    return render(request, 'base.html')