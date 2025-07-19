from django.shortcuts import redirect, render,get_object_or_404

from .models import Customer
from savingplan.models import SavingPlan, CustomerSaving
from .forms import CreateForm
from django.core.paginator import Paginator
from django.db.models import Q


def dashboard(request):
    customers = Customer.objects.all()

    total_customers = Customer.objects.count()

    context = {
        'customers': customers,
        'total_customers': total_customers,
    }
    return render(request, 'dashboard.html', context)


def customers(request):
    all_customers  = Customer.objects.all()
    customer_plan = SavingPlan.objects.all()
    customers_saving = CustomerSaving.objects.all()
    paginator = Paginator(all_customers, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'customer_plan': customer_plan,
        'customers_saving': customers_saving,
    }
    return render(request, 'customers.html', context)

def customer_details(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    context = {
        'customer': customer,
        'customer_plan': customer_plan,
        'customers_saving': customers_saving,
    }
    return render(request, 'customer_details.html', context)

def createuser(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers:customers')           
    else:
        form = CreateForm()
    return render(request, 'createuser.html', {'form': form})


def search_customers(request):
    query = request.GET.get('q', '')   #get the search term from the query
    if query:
        results = Customer.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(location__icontains=query) |
            Q(gender__icontains=query) |
            Q(business__icontains=query)
            )
    else: 
        results = []
    context = {
        'query':query,
        'results': results
    }
    return render(request, 'search_customer.html', context)


def edit_customer(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    if request.method == 'GET':
        context = {'form': CreateForm(instance=customer), 'id':id}
        return render(request, 'editcustomer.html', context)

    elif request.method == 'POST':
        form = CreateForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers:customer_details', pk=customer.pk)
        else:
            # messages.error(request, 'Please correct the following errors:')
            return render(request, 'editcustomer.html', {'form':form})
    
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers:customers')
    return render(request, 'confirm_delete.html', {'customer': customer})



