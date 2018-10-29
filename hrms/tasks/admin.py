from django.contrib import admin
from .task_models.base import BaseTask
from .task_models.development import DevelopmentTask
from .task_models.operations import OperationTask
# Register your models here.


admin.site.register(BaseTask)
admin.site.register(DevelopmentTask)
admin.site.register(OperationTask)