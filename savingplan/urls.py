from urls import path

from . import views

app_name = 'saving'

urlpatterns = [
    path('savings', views.CustomerSaving, name="customersavings")
]