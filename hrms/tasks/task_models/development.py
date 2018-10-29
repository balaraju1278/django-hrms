"""
    Author: Bala
    description: Development task models lives here
"""
from django.db import models
from django.utils.translation import ugettext as _

from .base import BaseTask
from people.models import Employee



class DevelopmentTask(BaseTask):
    """
        development task model
    """
    employees = models.ManyToManyField(Employee, verbose_name=_("Employees"))
    send_copy_email = models.BooleanField(default=True)
    instructions = models.TextField(verbose_name=_("Instructions"), blank=True, null=True)
    attachments = models.FileField(upload_to='tasks/', blank=True, null=True)
    

        
    def __str__(self):
        return self.title
    
    def get_status(self):
        """
            returns task status
        """
        if self.status:
            return self.status
        else:
            return "n/a"
    @staticmethod
    def send_email_copy(self):
       pass
    
    class Meta:
        verbose_name = _("Development Task")
        verbose_name_plural = _("Development Tasks")