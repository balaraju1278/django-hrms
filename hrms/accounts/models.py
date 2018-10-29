from django.db import models


# Create your models here.
class Invoice(models.Model):
    class Meta:
        verbose_name = "Invoice"


class Bill(models.Model):
    class Meta:
        verbose_name = "Bill"


class Quote(models.Model):
    class Meta:
        verbose_name = "Quotation"


class NDA(models.Model):
    class Meta:
        verbose_name = "NDA Aggrement"
    
    
class Aggriment(models.Model):
    class Meta:
        verbose_name = "Aggrement"
        
        
class Payment(models.Model):
    class Meta:
        verbose_name = "Payment"