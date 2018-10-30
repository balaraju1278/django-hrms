"""
    Author: Bala
    Description: Task Base admin models utils lives here
"""

from django.contrib import admin
from .task_models.base import BaseTask
from .task_models.development import DevelopmentTask
from .task_models.operations import OperationTask
# Register your models here.


class BaseTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'current_status', 'result_status')
    actions = []
admin.site.register(BaseTask, BaseTaskAdmin)

admin.site.register(DevelopmentTask)
admin.site.register(OperationTask)