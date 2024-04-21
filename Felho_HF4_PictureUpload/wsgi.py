"""
WSGI config for Felho_HF4_PictureUpload project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Felho_HF4_PictureUpload.settings')

application = get_wsgi_application()
