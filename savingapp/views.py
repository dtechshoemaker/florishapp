from django.shortcuts import render
from .models import Customer

def dashboard(request):
    customers = Customer.objects.all()
    return render(request, 'dashboard.html', {'customers':customers})


def customers(request):
    return render(request, 'customers.html')

