from django.db import models
from .c_models.customer import Customer
from .c_models.customer_project import CustomerProject
# Create your models here.



class CustomerBilling(models.Model):
    class Meta:
        verbose_name = "Customer Billing"


class CustomerInvoice(models.Model):
    class Meta:
        verbose_name = "Customer Invoice"