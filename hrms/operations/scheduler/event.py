"""
    Author: Bala
    Description: Company event models lives here ex:Outings, visitings, conferences, hackthons etc etc
"""

from django.db import models

class BaseEvent(models.Model):
    class Meta:
        verbose_name = "General Event"



class Outing(models.Model):
    class Meta:
        verbose_name = "Outings"



class Conference(models.Model):
    class Meta:
        verbose_name = "Conference"


class Hackathon(models.Model):
    class Meta:
        verbose_name = "Hackathon"



class TeamLunch(models.Model):
     class Meta:
        verbose_name = "Team Lunchs"
