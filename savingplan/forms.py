from django import forms
from django.forms import widgets

from .models import Contribution, SavingPlan, CustomerSaving

class SavingPlanForm(forms.ModelForm):
    class Meta:
        model = SavingPlan
        fields = ['name', 'amount_per_day', 'duration_in_days', 'start_date', 'end_date']

        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'amount_per_day': widgets.NumberInput(attrs={'class': 'form-control'}),
            'duration_in_days': widgets.NumberInput(attrs={'class': 'form-control'}),
            'start_date': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class CustomerSavingForm(forms.ModelForm):
    class Meta:
        model = CustomerSaving
        fields = ['customer', 'saving_plan', 'is_active', 'total_contributed']

        widgets = {
            'customer': widgets.Select(attrs={'class': 'form-control'}),
            'saving_plan': widgets.Select(attrs={'class': 'form-control'}),
            'is_active': widgets.CheckboxInput(attrs={'class': 'form-check-input'}),
            'total_contributed': widgets.NumberInput(attrs={'class': 'form-control'}),
        }
