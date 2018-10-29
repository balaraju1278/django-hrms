from django.db import models
"""
    author: Bala
    inhouse customer visit models lives here
"""

from django.utils import timezone
from django.utils.translation import ugettext as _

from operations.utils.postalaaddressprefix import POSTALADDRESSPREFIX
from people.models import Employee



class CustomerVisit(models.Model):
    """
        inhouse customer visit model
    """
    prefix = models.CharField(
                max_length=4, 
                choices=POSTALADDRESSPREFIX, 
                verbose_name=_("Prefix"), 
                blank=True, null=True )   
    first_name = models.CharField(
                max_length=100, 
                verbose_name=_("First Name"), 
                blank=True, null=True)
    last_name = models.CharField(
                max_length=100, 
                verbose_name=_("Last Name"), 
                blank=True, null=True)
    email = models.EmailField(
                max_length=150, 
                verbose_name=_("Email Id"), 
                blank=True, null=True)
    number = models.CharField(
                max_length=15, 
                verbose_name=_("Phone"), 
                blank=True, null=True)
    company = models.CharField(
                max_length=40, 
                verbose_name=_("Company Name"), 
                blank=True, null=True)
    designation = models.CharField(
                max_length=50, 
                verbose_name=_("Designation"), 
                blank=True, null=True)
    purpose = models.CharField(
                max_length=500, 
                verbose_name=_("Purpose"), 
                help_text=_("upto 500 chars"), 
                blank=True, null=True)
    description = models.TextField(
                verbose_name=_("Description"), 
                blank=True, null=True)
    comming_from = models.CharField(
                verbose_name=_("Coming From"), 
                blank=True, null=True, 
                help_text=_("Coming from city")) 
    visting_date = models.DateField(
                verbose_name=_("Visiting Date"))
    visitinig_time = models.DateTimeField(
                verbose_name=_("Visting Time"))
    meeting_with = models.ForeignKey(
                Employee, 
                verbose_name=_("Meeting With"))
    result_note = models.TextField(
                verbose_name=_("Result Summary"), 
                blank=True, null=True)
    
    def save_first_name(self, *args, **kwargs):
        self.first_name = self.first_name.lower()
        super(CustomerVisit, self).save(*args, **kwargs)
    
    def save_last_name(self, *args, **kwargs):
        self.last_name = self.last_name.lower()
        super(CustomerVisit, self).save(*args, **kwargs)
    
    def save_email(self, *args,**kwargs):
        self.email = self.email.lower()
        super(CustomerVisit, self).save(*args, **kwargs)
    
    def save_company(self, *args, **kwargs):
        self.company = self.comapny.lower()
        super(CustomerVisit, self).save(*args, **kwargs)
    
    def designation(self, *args, **kwargs):
        self.designation = self.desgination.lower()
        super(CustomerVisit, self).save(*args, **kwargs)
    
    def comming_from(self, *args, **kwargs):
        self.comming_from = self.comming_from.lower()
        super(CustomerVisit, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(CustomerVisit, self).save(*args, **kwargs)
        
    def get_full_name(self):
        """
            returns customer full name
        """
        if self.first_name & self.last_name:
            return self.first_name + '' + self.last_name
        else:
            return "n/a"
    
    def get_email(self):
        """
            returns customer email id
        """
        if self.email:
            return self.email
        else:
            return "n/a"
        
    def get_number(self):
        """
            returns customer contact number
        """
        if self.number:
            return self.number
        else:
            return "n/a"
    
    def get_meeting_with(self):
        """
            returns customer meething with whom
        """
        if self.meeting_with:
            return self.meeting_with
        else:
            return "n/a"
            
    
    def get_meeting_agenda(self):
        """
            returns customer visting agenda
        """
        if self.purpose:
            return self.purpose+ '==>' + self.employee
        else:
            return "n/a"
    