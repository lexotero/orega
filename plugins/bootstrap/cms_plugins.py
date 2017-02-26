# (c) 2017 Alejandro Otero Ortiz de Cosca

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin


class ContainerFluidPlugin(CMSPluginBase):
    name = 'Bootstrap container-fluid'
    model = CMSPlugin
    render_template = 'plugins/container-fluid.html'
    cache = False
    allow_children = True


class RowPlugin(CMSPluginBase):
    name = 'Bootstrap row'
    model = CMSPlugin
    render_template = 'plugins/row.html'
    cache = False
    allow_children = True


plugin_pool.register_plugin(ContainerFluidPlugin)
plugin_pool.register_plugin(RowPlugin)
