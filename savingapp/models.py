from django.db import models
from django.utils import timezone


AGBOLI = 'AG'
BIG_CHURCH = 'BC'
SMART_ROAD = 'SR'
DO_GOOD = 'DG'
FIKO_ROAD = 'FR'
BOSSY1_WATER = '1BW'
BOSSY2_WATER = '2BW'
TOMBIA_MARKET = 'TM'
SCHOOL_ROAD = 'SR'
ISKI = 'IS'
ETEGUE1 = 'ETE1'
ETEGUE2 = 'ETE2'
DEEPER1_LIFE = 'DP1'
DEEPER2_LIFE = 'DP2'
AMASOMA_ROAD = 'AMR'
EDEPIE = 'EDE'
AGUDAMA = 'AGU'

LOCATION_CHOICES = [
    ('AGBOLI', 'agboli'),
    ('BIG CHURCH', 'big_church'),
    ('SMART ROAD', 'smart_road'),
    ('DO GOOD', 'do_good'),
    ('FIKO ROAD', 'fiko_road'),
]

GENDER_CHOICES = [
    ('ML', 'male'),
    ('FE', 'female'),
]


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    location = models.CharField(max_length=200, choices=LOCATION_CHOICES, default=AGBOLI)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    business = models.CharField(max_length=200)
    create_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.first_name


DAILY = 'DL'

FREQUENCY_CHOICES = [
    ('DL', 'daily'),
    ('WL', 'weekly'),
    ('ML', 'monthly'),
]

class SavingPlan(models.Model):
    name = models.CharField(max_length=100)
    amount_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    duration_in_days = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CustomerSaving(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='savings')
    saving_plan = models.ForeignKey(SavingPlan, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    total_contributed = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.full_name} - {self.saving_plan.name}"

"""
Contribution is the daily payment by the user which will be used for the tabke
for the user
"""
class Contribution(models.Model):
    customer_saving = models.ForeignKey(CustomerSaving, on_delete=models.CASCADE, related_name='contributions')
    payment_date = models.DateField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_saving.customer.full_name} - {self.payment_date}"




    