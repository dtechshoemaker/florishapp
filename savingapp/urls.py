from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customers/', views.customers, name='customers'),
    path('customer/<int:pk>/', views.customer_details, name='customer_details'),
    path('customers/add-customer/', views.createuser, name='create-customer'),
]
