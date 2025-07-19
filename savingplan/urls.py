from django.urls import path

from . import views

app_name = 'savingsplan'

urlpatterns = [
    path('savings', views.customer_list, name="customersavings"),
    path('createplan', views.create_plan, name="createplan")
]