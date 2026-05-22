from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def menu(request):

    products = Product.objects.all()

    return render(request, 'choco_menu.html', {'products': products})


def contact(request):
    return render(request, 'contact.html')


def customize(request):
    return render(request, 'coco_costmize.html')


def payment(request):
    return render(request, 'c_pay.html')


def login(request):
    return render(request, 'logo_and_sin.html')