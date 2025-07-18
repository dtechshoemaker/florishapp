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
            'start_date': widgets.DateInput(attrs={'class': 'form-control'}),
            'end_date': widgets.DateInput(attrs={'class': 'form-control'}),
        }
