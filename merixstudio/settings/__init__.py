from django.core.exceptions import ImproperlyConfigured
try:
    from .local import *  # noqa
except ImportError:
    from .default import *  # noqa

if not DEBUG and SECRET_KEY == SECRET_SENTINEL:
    raise ImproperlyConfigured("Replace SECRET_KEY value in settings/local.py")
