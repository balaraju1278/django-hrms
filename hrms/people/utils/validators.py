import unicodedata

from confusable_homoglyphs import confusables
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import six
from django.utils.translation import ugettext_lazy as _



DEPARTMENT = {
    'INVALID_NAME': _("Please Enter a Valid Department Name in Correct Format"),
    'INVALID_CODE': _("Please Enter a Valid Department Code"),
    'INVALID_DP_HEAD': _("Please Enter a Valid Person Name"),
    'INVALID_DP_MAIL': _("Please Enter a Valid Email Id")
}


EMPLOYEE = {
    'INVALID_FIRST_NAME': _("Please Enter a Valid First Name in Correct Format"),
    'INVALID_LAST_NAME': _("Please Enter a Valid Last Name in Correct Format"),
    'INVALID_DOB': _("Please Enter a Valid date of birth"),
    'INVALID_EMP_CODE' : _("Please Enter a Valid Emplooye ID"),
    'INVALID_CMAIL': _("Please Enter a Valid company Email"),
    'INVALID_JD': _("Please Enter a Valid Joining Date"),
}

EMP_DESIGNATION = {
    'INVALID_TITLE': _("Please Enter a Valid Designation title"),
}
RESERVED_NAME =  _(u"This name is reserved and cannot be registered.") 


SPECIAL_HOSTNAMES = [
    # Hostnames with special/reserved meaning.
    'autoconfig',     # Thunderbird autoconfig
    'autodiscover',   # MS Outlook/Exchange autoconfig
    'broadcasthost',  # Network broadcast hostname
    'isatap',         # IPv6 tunnel autodiscovery
    'localdomain',    # Loopback
    'localhost',      # Loopback
    'wpad',           # Proxy autodiscovery
    'nginx',
    'redis',
    'rabbitmq',
    'celery'
    'docker',
    'chef',
    'ansibel',
    'cloud',
    'aws',
    'amazon',
    'azure',
    'digital',
    'rockspace',
    
]

PROTOCOL_HOSTNAMES = [
    # Common protocol hostnames.
    'ftp',
    'imap',
    'mail',
    'news',
    'pop',
    'pop3',
    'smtp',
    'usenet',
    'uucp',
    'webmail',
    'www',
]

CA_ADDRESSES = [
    # Email addresses known used by certificate authorities during
    # verification.
    'admin',
    'administrator',
    'hostmaster',
    'info',
    'is',
    'it',
    'mis',
    'postmaster',
    'root',
    'ssladmin',
    'ssladministrator',
    'sslwebmaster',
    'sysadmin',
    'webmaster',
]
RFC_2142 = [
    # RFC-2142-defined names not already covered.
    'abuse',
    'marketing',
    'noc',
    'sales',
    'security',
    'support',
]

NOREPLY_ADDRESSES = [
    # Common no-reply email addresses.
    'mailer-daemon',
    'nobody',
    'noreply',
    'no-reply',
]


SENSITIVE_FILENAMES = [
    # Sensitive filenames.
    'clientaccesspolicy.xml',  # Silverlight cross-domain policy file.
    'crossdomain.xml',         # Flash cross-domain policy file.
    'favicon.ico',
    'humans.txt',
    'keybase.txt',  # Keybase ownership-verification URL.
    'robots.txt',
    '.htaccess',
    '.htpasswd',
]

OTHER_SENSITIVE_NAMES = [
    # Other names which could be problems depending on URL/subdomain
    # structure.
    'account',
    'accounts',
    'auth',
    'authorize',
    'blog',
    'buy',
    'cart',
    'clients',
    'contact',
    'contactus',
    'contact-us',
    'copyright',
    'dashboard',
    'doc',
    'docs',
    'download',
    'downloads',
    'enquiry',
    'faq',
    'help',
    'inquiry',
    'license',
    'login',
    'logout',
    'me',
    'myaccount',
    'oauth',
    'pay',
    'payment',
    'payments',
    'plans',
    'portfolio',
    'preferences',
    'pricing',
    'privacy',
    'profile',
    'register',
    'secure',
    'settings',
    'signin',
    'signup',
    'ssl',
    'status',
    'store',
    'subscribe',
    'terms',
    'tos',
    'user',
    'users',
    'weblog',
    'work',
]
DEFAULT_RESERVED_NAMES = (
    SPECIAL_HOSTNAMES + PROTOCOL_HOSTNAMES + CA_ADDRESSES + RFC_2142 +
    NOREPLY_ADDRESSES + SENSITIVE_FILENAMES + OTHER_SENSITIVE_NAMES
)


class ReservedNameValidator(object):
    """
        validator that disallowed reserved names
    """
    
    def __init__(self, reserved_names_list=DEFAULT_RESERVED_NAMES, *args, **kwargs):
            self.reserved_names_list = reserved_names_list
    
    def __call__(self, value):
        if not isinstance(value, six.text_type):
            return
        
        if value in self.reserved_names_list or value.startswith('.well-known'):
            raise ValidationError(
                RESERVED_NAME, code='invalid'            
            )


class CaseInsenstiveUnique(object):

    def __init__(self, model, field_name, error_msg, *args, **kwargs):
        self.model = model
        self.field_name = field_name
        self.error_msg = error_msg
    
    def __call__(self, value):
        if not isinstance(value, six.text_type):
            return
        
        value = unicodedata.normalize("NFKC", value)
        if hasattr(value, 'casefold'):
            value = value.casefold()
        if self.model._default_manager.filter(**{'{}__iexact'.format(self.field_name): value}).exists():
            raise ValidationError(self.error_msg, code='unique')
        
        def validate_confusable_user_names(value):
            if not isinstance(value, six.text_type):
                return
            if confusables.is_dangerous(value):
                raise ValidationError("", code='invalid')