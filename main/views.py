from django.shortcuts import render

from .models import Product

def menu(request):

    products = Product.objects.all()

    return render(request, 'choco_menu.html', {'products': products})