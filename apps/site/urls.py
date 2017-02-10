# (c) 2017 Orega S.L.

from django.conf.urls import url

from apps.site.views import (
    AboutView,
    QualityAndEnvironmentView,
)

urlpatterns = [
    # url(r'$', name='home', view=''),
    url(r'^calidad-y-medioambiente/', view=QualityAndEnvironmentView.as_view(), name='calidad-y-medioambiente'),
    # url(r'^contacto/', view='', name='contacto'),
    # url(r'^proyectos/', view='', name='proyectos'),
    url(r'^sobre-nosotros/', view=AboutView.as_view(), name='sobre-nosotros'),
]
