"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from config.settings import base

if base.DEBUG:
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "config.settings.local",
    )
else:
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "config.settings.production",
    )

application = get_asgi_application()
