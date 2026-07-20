from django.shortcuts import render
from .models import Product
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

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


def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('logged_home')

        else:
            return render(request, 'logo_and_sin.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'logo_and_sin.html')
def logged_home(request):
    return render(request, 'home_logged.html')

def register_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # create new user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        login(request, user)

        return redirect('logged_home')
    
    def register_view(request):

      if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        login(request, user)

        return redirect('logged_home')

    return render(request, 'register.html')

    return render(request, 'register.html')