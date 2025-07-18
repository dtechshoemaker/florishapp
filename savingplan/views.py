from django.shortcuts import redirect, render

from .forms import SavingPlanForm

# Create your views here.

def CustomerSaving(request):
    if request.method == 'POST':
        form = SavingPlanForm(reuest.POST)
        if form.is_valid():
            form.save()
            return redirect('savings:customersavings')
    else:
        form = SavingPlanForm()

        context = {
            'form': form
        }
    return render(request, './savings/customersavings.html', context)
