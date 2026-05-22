from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),

    path('about/', about, name='about'),

    path('menu/', menu, name='menu'),

    path('contact/', contact, name='contact'),

    path('customize/', customize, name='customize'),

    path('payment/', payment, name='payment'),

    path('login/', login, name='login'),
]