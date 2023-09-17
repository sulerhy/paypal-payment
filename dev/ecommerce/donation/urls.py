from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.my_donation, name=''),
    path('payment-success', views.payment_success, name='payment-success'),
    path('payment-failed', views.payment_failed, name='payment-failed'),
]
