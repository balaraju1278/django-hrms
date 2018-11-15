
SERVER_EMAIL = 'root@localhost'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Host for sending email.
EMAIL_HOST = 'localhost'
# Port for sending email.
EMAIL_PORT = 25

EMAIL_USE_LOCALTIME = False
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None
EMAIL_TIMEOUT = None

# List of strings representing installed apps.
INSTALLED_APPS = []

TEMPLATES = []

# Default form rendering class.
FORM_RENDERER = 'django.forms.renderers.DjangoTemplates'


# Default email address to use for various automated correspondence from
# the site managers.
DEFAULT_FROM_EMAIL = 'webmaster@localhost'

EMAIL_SUBJECT_PREFIX = '[HRMS] '
