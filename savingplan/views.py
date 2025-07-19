from django.shortcuts import redirect, render, get_object_or_404

from .forms import SavingPlanForm, CustomerSavingForm
from .models import CustomerSaving, Contribution
from savingapp.models import Customer
from datetime import timedelta, date

# Create your views here.
def create_plan(request):
    if request.method == 'POST':
        form = SavingPlanForm(request.POST)
    else:
        form = SavingPlanForm()

    context = {
        'form': form
    }
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('savingsplan:customersavings')

    return render(request, './savings/createplan.html', context)

def create_customer_saving(request):
    customers = Customer.objects.all()
    if request.method == 'POST':
        form = CustomerSavingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('savingsplan:customersavings')
    else:
        form = CustomerSavingForm()

    context = {
        'form': form,
        'customers': customers
    }
    return render(request, './savings/create_savings.html', context)

def customer_saving_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    saving = CustomerSaving.objects.filter(customer=customer).first()

    if not saving:
        return render(request, './savings/customer_saving_details.html', {
            'customer': customer,
            'error': 'No active saving plan for this customer.'
        })

    today = date.today()
    days = [today - timedelta(days=i) for i in range(29, -1, -1)]  # last 30 days

    contributions = Contribution.objects.filter(
        customer_saving=saving,
        payment_date__range=(days[0], days[-1])
    ).values_list('payment_date', flat=True)

    paid_dates = set(contributions)
    records = []

    for day in days:
        paid = day in paid_dates
        records.append({
            'date': day,
            'paid': paid,
            'amount': saving.saving_plan.amount_per_day if paid else 0
        })

    total_paid = sum(r['amount'] for r in records)
    missed_days = len([r for r in records if not r['paid']])
    rate = round((30 - missed_days) / 30 * 100, 2)

    return render(request, './savings/customer_saving_details.html', {
        'customer': customer,
        'saving': saving,
        'records': records,
        'total_paid': total_paid,
        'missed_days': missed_days,
        'rate': rate
    })


def customer_list(request):
    customers = Customer.objects.filter()
    # Attach active savings to each customer
    for customer in customers:
        customer.saving = CustomerSaving.objects.filter(customer=customer, is_active=True).first()

    return render(request, './savings/customersavings.html', {'customers': customers})

    



def customer_saving_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    saving = CustomerSaving.objects.filter(customer=customer, is_active=True).first()

    if not saving:
        return render(request, 'customer_detail.html', {
            'customer': customer,
            'error': 'No active saving plan for this customer.'
        })

    today = date.today()
    days = [today - timedelta(days=i) for i in range(29, -1, -1)]  # last 30 days

    contributions = Contribution.objects.filter(
        customer_saving=saving,
        payment_date__range=(days[0], days[-1])
    ).values_list('payment_date', flat=True)

    paid_dates = set(contributions)
    records = []

    for day in days:
        paid = day in paid_dates
        records.append({
            'date': day,
            'paid': paid,
            'amount': saving.saving_plan.amount_per_day if paid else 0
        })

    total_paid = sum(r['amount'] for r in records)
    missed_days = len([r for r in records if not r['paid']])
    rate = round((30 - missed_days) / 30 * 100, 2)

    return render(request, './savings/customer_saving_details.html', {
        'customer': customer,
        'saving': saving,
        'records': records,
        'total_paid': total_paid,
        'missed_days': missed_days,
        'rate': rate
    })
