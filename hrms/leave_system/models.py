"""
    Author: Bala
    Description: leave models lives here
"""
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string
from django.core.validators import MaxValueValidator
from datetime import timedelta

from people.models import Employee
# Create your models here.


class LeaveCategory(models.Model):
    """
        The Typ of leave, ex: casual leave, medical leave
    """
    LEAVE_TYPES = (
        ('CL', 'Casual Leave'),
        ('ML', 'Medical Leave'),
        ('WH', 'Work From Homw'),    
    )    
    type_of_leave = models.CharField(max_length=25, choices=LEAVE_TYPES, null=True, blank=True, verbose_name=_("Leave Type"))
    number_of_days = models.PositiveIntegerField(
        validators = [MaxValueValidator(9999999999)]    
    )
    
    def __str__(self):
        return self.type_of_leave
        
    class Meta:
        verbose_name = _("Leave Categories")
        verbose_name_plural = _("Leave Categories")


class EmployeeLeaveProfile(models.Model):
    """
        Data we need for employee
    """
    employee = models.OneToOneField(Employee, verbose_name=_("Empplooye"))
    total_leaves = models.PositiveIntegerField(
                    validators=[MaxValueValidator(99999999999)]    
    )
    
    def __str__(self):
        return self.employee.pref_name
    
    def get_total_leaves(self):
        """
        returns totel leaves
        """
        if self.total_leaves:
            return self.total_leaves
        else:
            return "n/a"
    
    def employee_display(self):
        if self.employee.first_name and self.employee.last_name:
            return "%s %s" % (self.employee.first_name, self.emmployee.last_name)
        elif self.employee.first_name:
            return self.employee.first_name
        elif self.employee.last_name:
            return self.employee.last_name
        elif self.employee.pref_name:
            return self.employee.pref_name
        else:
            return self.employee.emp_code
            
    class Meta:
        verbose_name = _("Employee Leave Profiles")
        verbose_name_plural = _("Employee Leave Profiles")

def create_employee_profile(sender, **kwargs):
    instance = kwargs['instance']
    if kwargs['created']:
        EmployeeLeaveProfile.objects.create(employee=instance, total_leaves=settings.LEAVE_CONST)
post_save.connect(create_employee_profile, sender=Employee)


class LeaveApplication(models.Model):
    """
        Leave application 
    """
    start_date = models.DateField()
    end_date = models.DateField()
    num_of_days = models.IntegerField()
    employee = models.ForeignKey(EmployeeLeaveProfile)
    leave_category = models.ForeignKey("LeaveCategory")
    status = models.BooleanField(default=False)
    subject = models.CharField(max_length=500)
    body = models.TextField()
    
    def __str__(self):
        return "{} {}".format(self.employee, self.start_date)
        
    @property
    def employee(self):
        return self.employee
    
    @property
    def status_display(self):
        if self.status:
            return "Approved"
        else:
            return "Requested"

def send_approval_mail(sender, **kwargs):
    pass

def modify_num_of_days(sender, **kwargs):
    pass

def change_user_name(sender, **kwargs):
    pass