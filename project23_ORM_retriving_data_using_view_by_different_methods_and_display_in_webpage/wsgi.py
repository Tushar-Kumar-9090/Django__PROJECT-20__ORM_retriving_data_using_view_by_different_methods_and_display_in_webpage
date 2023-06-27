"""
WSGI config for project23_ORM_retriving_data_using_view_by_different_methods_and_display_in_webpage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project23_ORM_retriving_data_using_view_by_different_methods_and_display_in_webpage.settings')

application = get_wsgi_application()
