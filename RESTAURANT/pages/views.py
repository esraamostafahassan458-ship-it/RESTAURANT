from django.shortcuts import render
from .models import MenuItem

def home(request):
    return render(request, 'pages/home.html')

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'pages/menu.html', {'items': items})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')


# Create your views here.
