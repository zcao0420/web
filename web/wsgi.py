"""
WSGI config for web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from os.path import dirname,abspath

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
os.environ.setdefault("PYTHON_EGG_CACHE", "/tmp/.python-eggs")
PROJECT_DIR = dirname(dirname(abspath(__file__)))

sys.path.insert(0,PROJECT_DIR)

application = get_wsgi_application()
