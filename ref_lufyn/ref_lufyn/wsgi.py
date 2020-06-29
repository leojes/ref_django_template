"""
WSGI config for ref_lufyn project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ref_lufyn.settings')
# add staging in settings and also here.
os.environ.setdefault('DJANGO_CONFIGURATION', 'Production')

application = get_wsgi_application()
