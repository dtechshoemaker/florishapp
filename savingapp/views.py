from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse
from .models import Customer

def dashboard(request):
    customers = Customer.objects.all()
    return render(request, 'dashboard.html', {'customers':customers})


def customers(request):
    customers = Customer.objects.all()

    context = {
        'customers': customers
    }
    return render(request, 'customers.html', context)

def customer_details(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    context = {
        'customer': customer
    }
    return render(request, 'customer_details.html', context)

def createuser(request):
    return render(request, 'createuser.html')


