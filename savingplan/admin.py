from django.contrib import admin

from .models import SavingPlan, CustomerSaving, Contribution

# Register your models here.

admin.site.register(SavingPlan)
admin.site.register(CustomerSaving)
admin.site.register(Contribution)
