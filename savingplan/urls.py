from django.urls import path

from . import views

app_name = 'savingsplan'

urlpatterns = [
    path('savings', views.customer_list, name="customersavings"),
    path('createplan', views.create_plan, name="createplan"),
    path('createcustomersaving/', views.create_customer_saving, name="createcustomersaving"),
    path('customersaving/<int:customer_id>/', views.customer_saving_detail, name="customer_saving_details"),
]