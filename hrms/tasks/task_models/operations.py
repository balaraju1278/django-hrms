"""
    Author: Bala
    description: Operation task models lives here
"""
from django.db import models
from django.utils.translation import ugettext as _

from people.models import Employee
from .base import BaseTask,TaskAttachmentFile


class OperationTask(BaseTask):
    """
        Operations task model
    """
    employee = models.ForeignKey(
                        Employee, 
                        verbose_name=_("Employee"))
    send_copy_email = models.BooleanField(default=True)
    instructions = models.TextField(
                        verbose_name=_("Instructions"), 
                        blank=True, null=True)
    
    attachment = models.ForeignKey(
                         TaskAttachmentFile, 
                         verbose_name=_("Attchement"))
    def __str__(self):
        return self.title
    
    @property    
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
    
    def clean(self, *args, **kwrgs):
        """
            validates type and convert to lower case
        """
        if self.instructions:
            self.instructions = self.instructions.lower()
    
    def save(self, *args, **kwargs):
        """
            saving to db and sending an email copy to
            emplooys and reviewer
        """
        # impliment send a copy mail to employees and reviewer
        super(self.__class__, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = _("Operation Task")
        verbose_name_plural = _("Operation Tasks")