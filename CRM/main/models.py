import django.utils.timezone
from django.db import models

class CRM_model(models.Model):
    QUALITY_CHOICES = [
        ('C', 'Normal'),
        ('B', 'Good'),
        ('A', 'Medium'),
        ('S', 'Premium'),
        ('SS', 'Elite'),
    ]
    customer_name = models.CharField(max_length=50, null=True, unique=False)
    date = models.DateField(default=django.utils.timezone.now)
    expiry_date = models.DateField()
    product_description = models.TextField(max_length=250, null=False, unique=False, default='Описания нет')
    price = models.DecimalField(null=False, unique=False, decimal_places=2, max_digits=7, default=0)
    contacts = models.CharField(null=False, max_length=60)
    quality = models.CharField(max_length=15, choices=QUALITY_CHOICES, default='A')
    type = models.CharField(max_length=20, null=True, unique=False)
    checkbox = models.BooleanField(default=False, null=False)
    complete_date = models.DateField(null=True, unique=False)

    def __str__(self):
        return f'{self.customer_name}, {self.product_description}, {self.quality}, {self.expiry_date}'