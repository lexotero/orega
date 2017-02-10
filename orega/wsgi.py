# (c) 2017 Orega S.L.

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orega.settings.production")

application = get_wsgi_application()
