# (c) 2017 Orega S.L.

from orega.settings.defaults import *

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
