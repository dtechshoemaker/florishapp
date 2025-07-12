from django.forms import ModelForm
from .models import Customer


class CreateForm(ModelForm):
    class meta:
        model = Customer
        fiels = '__all__'