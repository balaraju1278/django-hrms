"""
    Author: Bala
    Description: Employee visting models lives here
"""


from django.db import models
import datetime
from django.contrib import admin
from django.utils import timezone

from django.utils.translation import ugettext as _
from operations.utils.status import CALL_STATUS
from .base import Person
from people.models import Employee


class EmployeeVisit(models.Model):
    """
        employee visit model
    """
    employee = models.ForeignKey(
                Employee, 
                verbose_name=_("Staff Employee"))
    visiting_company = models.CharField(
                max_length=100, 
                verbose_name=_("Visiting Company"))
    purpose = models.CharField(
                max_length=500, 
                verbose_name=_("Purpose"), 
                help_text=_("upto 500 chars"), 
                blank=True, null=True)
    description = models.TextField(
                verbose_name=_("Description"), 
                blank=True, null=True)
    visting_date = models.DateField(
                verbose_name=_("Meeting Date"))
    visiting_city = models.CharField(
                verbose_name=_("Meeting City"), 
                max_length=100, 
                null=True, blank=True)
    contact_person = models.CharField(
                verbose_name=_("Meeting With"), 
                max_length=100, 
                null=True, blank=True)
    contact_person_designation = models.CharField(
                verbose_name=_("Designation"), 
                max_length=100, 
                null=True, blank=True)
    result_note = models.TextField(
                verbose_name=_("Result Summary"), 
                blank=True, null=True)
    
    def save_visiting_company(self,*args, **kwargs):
        self.visting_company = self.visiting_company.lower()
        super(EmployeeVisit, self).save(*args, **kwargs)
    
    def save_purpose(self, *args, **kwargs):
        self.purpose = self.purpose.lower()
        super(EmployeeVisit, self).save(*args, **kwargs)
    
    def save_contact_person(self, *args, **kwargs):
        self.contact_person = self.contact_person.lower()
        super(EmployeeVisit, self).save(*args, **kwargs)
    
    def save_contact_person_designation(self, *args, **kwargs):
        self.contact_person_designation = self.contact_person_designation.lower()
        super(EmployeeVisit, self).save(*args, **kwargs)
    
    def save_result_note(self, *args, **kwargs):
        self.result_note = self.result_note.lower()
        super(EmployeeVisit, self).save(*args, **kwargs)
        
    def get_visiting_company(self):
        """
            returns employee visiting company
        """
        if self.visiting_company:
            return self.visting_company
        else:
            return "n/a"
    
    def get_contact_person(self):
        """
            returns employee contact person
        """
        if self.contact_person:
            return self.contact_person
        else:
            return "n/a"
    
    def get_result_note(self):
        """
            returns employee visit result
        """
        if self.result_note:
            return self.result_note
        else:
            return "n/a"
    
    def get_visiting_agenda(self):
        """
            returns visiting agend
        """
        if self.purpose:
            return self.purpose
        else:
            return "n/a"
    
    class Meta:
        verbose_name = _("Employee visits")
        verbose_name_plural = _("Employee Visits")