from django.contrib import admin

from .models import Customer, Contribution

admin.site.register(Customer)
admin.site.register(Contribution)