from django.db import models
from savingapp.models import Customer
from django.utils import timezone

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
    saving_plan = models.ForeignKey(SavingPlan, on_delete=models.CASCADE, blank="True", null="none",)
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
    customer_saving = models.ForeignKey(
        CustomerSaving,
        null=True,  # allow saving without this value (optional)
        blank=True,
        on_delete=models.CASCADE,
        related_name='contributions'
    )
    payment_date = models.DateField(default=timezone.now)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.customer_saving and self.customer_saving.customer:
            return f"{self.customer_saving.customer.full_name} - {self.payment_date}"
        return f"Unknown Customer - {self.payment_date}"