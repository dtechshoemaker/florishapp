from django.db import models

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
    ('BIG_CHURCH', 'big_church'),
    ('SMART_ROAD', 'smart_road'),
    ('DO_GOOD', 'do_good'),
    ('FIKO_ROAD', 'fiko_road'),
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


    def __str__(self):
        return self.first_name

DAILY = 'DL'


FREQUENCY_CHOICES = [
    ('DL', 'daily'),
    ('WL', 'weekly'),
    ('ML', 'monthly'),
]

class Contribution(models.Model):
    name = models.CharField(help_text="name of saving", max_length=100, default="Mr Something")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, max_length=200)
    frequency = models.CharField(max_length=200, choices=FREQUENCY_CHOICES, default=DAILY)
    amount = models.IntegerField()
    start_date = models.DateTimeField()

    def __str__(self):
        return self.name




    