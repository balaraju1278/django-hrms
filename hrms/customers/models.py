from django.db import models
from .c_models.customer import Customer
# Create your models here.


class CustomerProject(models.Model):
    class Meta:
        verbose_name = "Customer Project"


class CustomerBilling(models.Model):
    class Meta:
        verbose_name = "Customer Billing"


class CustomerInvoice(models.Model):
    class Meta:
        verbose_name = "Customer Invoice"