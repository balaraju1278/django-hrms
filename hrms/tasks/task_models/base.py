"""
    Author: Bala
    Description: Task Base models utils lives here
"""
from django.db import models
from django.utils.translation import ugettext as _


class BaseTask(models.Model):
    """
        base task model
    """
    HIGH = 'H'
    LOW = 'L'
    NORMAL = 'N'
    
    PRIORITY_CHOICES = (
        ('H', 'HIGH'),
        ('L', 'LOW'),
        ('N', 'NORMAL'),    
    )
    
    TASK_STATUS = (
        ('C', 'COMPLETED'),
        ('ON', 'ONGOING'),    
    )
    
    title = models.CharField(
            max_length=150, 
            verbose_name=_("Title"), 
            blank=True, null=True)
    description = models.TextField(
            verbose_name=_("Description"), 
            blank=True, null=True)
    priority = models.CharField(
            max_length=6, 
            verbose_name=_("Priority"), 
            blank=True, null=True)    
    created_at = models.DateTimeField(
            auto_now_add=True,
            verbose_name=_("Created At"), 
            blank=True, null=True)
    due_date = models.DateField(
            verbose_name=_("Due Date"), 
            blank=True, null=True)
    
    status = models.CharField(
            verbose_name=_("Status"), 
            blank=True, null=True, 
            max_length=10)
            
    def __str__(self):
        return self.title
    
    def get_title(self):
        """
            returns title of task
        """
        if self.title:
            return self.title
        else:
            return "n/a"
    
    def get_due_date(self):
        """
            returns due date of task
        """
        if self.due_date:
            return self.due_date.strftime("%d, %b, %Y")
        else:
            return "n/a"
    
    def ger_remaining_days(self):
        """
            returns remaing days of task
        """
        if self.created_at & self.due_date:
            c_date = self.created_at
            d_date = self.due_date
            rm_days = d_date-c_date
            return rm_days.strftime("%d, %b, %Y")
        else:
            return "This task is TBD"
    
    class Meta:
        verbose_name = _("Base Tasks")
        verbose_name_plural = _("Base Tasks")