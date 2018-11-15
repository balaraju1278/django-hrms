from django.apps import AppConfig
from django.contrib.admin.checks import check_admin_app, check_dependencies
from django.core import checks
from django.utils.translation import ugettext_lazy as _


class HRMSPeopleConfig(AppConfig):
    
    default_site = 'django.contrib.admin.sites.AdminSite'
    name = 'django_hrms.contribute.people'
    verbose_name = _("People Management")

    def ready(self):
        checks.register(check_dependencies, checks.Tags.admin)
        checks.register(check_admin_app, checks.Tags.admin)


class PeopleConfig(HRMSPeopleConfig):
    
    def ready(self):
        super().ready()
        self.module.autodiscover()
