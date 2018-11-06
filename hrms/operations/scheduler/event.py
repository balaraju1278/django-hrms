"""
    Author: Bala
    Description: Company event models lives here ex:Outings, visitings, conferences, hackthons etc etc
"""

from django.db import models
from people.models import Employee


class BaseEvent(models.Model):
    
    name = models.CharField(max_length=150)
    venue = models.CharField(max_length=300)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    attending_employees = models.ManyToManyField(Employee)
    
    class Meta:
        verbose_name = "General Event"


class Outing(BaseEvent):
    location = models.CharField(max_length=150)
    
    class Meta:
        verbose_name = "Outings"



class Conference(BaseEvent):
    location = models.CharField(max_length=150)
    
    class Meta:
        verbose_name = "Conference"


class Hackathon(BaseEvent):
    location = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Hackathon"



class TeamLunch(BaseEvent):
    location = models.CharField(max_length=150)
    
    class Meta:
        verbose_name = "Team Lunchs"
