from django.contrib import admin

from .models import customer, contribution

admin.site.register(customer)
admin.site.register(contribution)