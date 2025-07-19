from django import forms
from .models import Customer

class CreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'location', 'address', 'phone', 'gender', 'business']


        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control py-3',
                'placeholder': 'First Name Here...'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number here...'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name Here...'
            }),
            'location': forms.Select(attrs={
                'class': 'form-control'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address here...'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control'
            }),
            'business': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Business type here...'
            })
        }
