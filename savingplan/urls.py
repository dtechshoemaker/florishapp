from django.urls import path

from . import views

app_name = 'savingsplan'

urlpatterns = [
    path('savings', views.CustomerSaving, name="customersavings")
]