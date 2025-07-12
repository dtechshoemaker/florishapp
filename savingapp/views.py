from django.shortcuts import render,get_object_or_404

from .models import Customer
from .forms import CreateForm
from django.core.paginator import Paginator


def dashboard(request):
    customers = Customer.objects.all()
    return render(request, 'dashboard.html', {'customers':customers})


def customers(request):
    all_customers  = Customer.objects.all()

    paginator = Paginator(all_customers, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    return render(request, 'customers.html', context)

def customer_details(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    context = {
        'customer': customer
    }
    return render(request, 'customer_details.html', context)

def createuser(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateForm()
    return render(request, 'createuser.html', {'form': form})


