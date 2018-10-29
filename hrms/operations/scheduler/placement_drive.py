"""
    Author: Bala
    Description: Placement drive models lives here
"""

from django.db import models
from django.utils.translation import ugettext as _


class RecruitmentDrive(models.Model):
    """
        recruitment drive model
        note: keep as it is later normalization will be required
    """
    institute = models.CharField(
                max_length=100, unique=True,
                verbose_name=_("Institute"), 
                blank=True, null=True)
    contact_person = models.CharField(
                max_length=100, 
                verbose_name=_("Contact Person"), 
                blank=True, null=True)
    contact_email = models.CharField(
                max_length=100, unique=True,
                verbose_name=_("Contact Email"), 
                blank=True, null=True)
    contact_number = models.CharField(
                max_length=14, unique=True,
                null=True, blank=True, 
                verbose_name=_("Contact Number"))
    address_one = models.CharField(
                max_length=200, 
                null=True, blank=True, 
                verbose_name=_("Address Line"))
    street_name = models.CharField(
                max_length=100, 
                null=True, blank=True, 
                verbose_name=_("Street Name"))
    city = models.CharField(
                max_length=100, 
                null=True, blank=True, 
                verbose_name=_("City"))
    state = models.CharField(
                max_length=100, 
                null=True, blank=True, 
                verbose_name=_("State"))
    country = models.CharField(
                max_length=100, 
                null=True, blank=True, 
                verbose_name=_("Country"))
    pincode = models.CharField(
                max_length=6, 
                null=True, blank=True, 
                verbose_name=_("Pincode"))
    drive_date = models.DateField(
                verbose_name=_("Drive Date"))
    hired_candidates = models.CharField(
                verbose_name=_("Total Selected Candidates"), 
                max_length=3, 
                blank=True, null=True)
    
    def __str__(self):
        return self.institute + '==>' + self.drive_date
    
    def get_institute(self):
        """
            returns institute name
        """
        if self.institute:
            return self.institute
        else:
            return "n/a"
    
    def get_drive_date(self):
        """
            returns drive date
        """
        if self.drive_date:
            return self.drive_date
        else:
            return "n/a"
    
    def get_contact_person(self):
        """
            returns institute contact person
        """
        if self.contact_person:
            return self.contact_person
        else:
            return "n/a"
    
    def get_contact_email(self):
        """
            returns institute contact email
        """
        if self.contact_email:
            return self.contact_email
        else:
            return "n/a"
    
    def get_contact_number(self):
        """
            returns institute contact number
        """        
        if self.contact_number:
            return self.contact_number
        else:
            return "n/a"
    
    class Meta:
        verbose_name = _("Yottaasys Drives")
        verbose_name_plural = _("Yottaasys Drives")
        
    
class InstituteAddress(models.Model):
    pass