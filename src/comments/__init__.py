import logging
from django.conf import settings

if settings.DEBUG == True and hasattr(settings, 'LOGGING'):
  logger = logging.getLogger(__name__)