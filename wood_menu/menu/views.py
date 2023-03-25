from django.shortcuts import render
from .models import Menu


# Create your views here.

def home(request):
    menus = Menu.objects.all()
    return render(request, 'menu/home.html', {'menus':menus})