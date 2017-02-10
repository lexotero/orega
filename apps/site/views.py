# (c) 2017 Orega S.L.

from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView


class TitledView(TemplateView):
    """ Simple TemplateView with the 'title' for the HTML inside the context. """
    title = ''

    def get_context_data(self, **kwargs):
        context_data = super(TitledView, self).get_context_data(**kwargs)
        context_data['title'] = self.title
        return context_data


class AboutView(TitledView):
    """
    This is the Class View for 'sobre nosotros' page.
    """
    template_name = 'site/base.html'
    title = _('Sobre nosotros')


class QualityAndEnvironmentView(TitledView):
    """
    This is the Class view for 'calidad y medioambiente' page.
    """
    template_name = 'site/base.html'
    title = _('Calidad y Medioambiente')