from django.db import models
from django.utils.translation import ugettext as _

from people.models import Employee
from .base import BaseTask


class OperationTask(BaseTask):
    """
        Operations task model
    """
    employee = models.ForeignKey(Employee, verbose_name=_("Employee"))
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
        verbose_name = _("Operation Task")
        verbose_name_plural = _("Operation Tasks")