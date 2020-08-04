"""
WSGI config for itScience project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itScience.settings')

configuration= os.path.dirname(__file__)
project = os.path.dirname(configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append(project)

application = get_wsgi_application()
