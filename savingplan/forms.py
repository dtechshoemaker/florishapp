from django import forms
from django.forms import widgets

from .models import Contribution, SavingPlan, CustomerSaving

class SavingPlanForm(forms.ModelForm):
    class Meta:
        Models = SavingPlan
        fields = '__all__'

        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'amount_per_day': widgets.NumberInput(attrs={'class': 'form-control'}),
            'duration_in_days': widgets.NumberInput(attrs={'class': 'form-control'}),
            'start_date': widgets.DateInput(attrs={'class': 'form-control'}),
            'end_date': widgets.DateInput(attrs={'class': 'form-control'}),
        }
