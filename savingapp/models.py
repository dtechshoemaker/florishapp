from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


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
    phone = models.CharField(max_length=200, default="none", blank=True, null=True)
    address = models.CharField(max_length=300)
    location = models.CharField(max_length=200, choices=LOCATION_CHOICES, default=AGBOLI)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    business = models.CharField(max_length=200)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name

    def clean(self):
        if Customer.objects.filter(first_name=self.first_name, last_name=self.last_name).exists():
            raise ValidationError("Customer with the same first name and last name already exists.")






    