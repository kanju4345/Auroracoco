from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('customize/', views.customize, name='customize'),
    path('payment/', views.payment, name='payment'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logged-home/', views.logged_home, name='logged_home'),
   
]