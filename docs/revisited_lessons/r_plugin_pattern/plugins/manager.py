from typing import Any

import pluggy

from . import PLUGIN_NAMESPACE
from .models import SpellPluginImpl, SpellPluginSpec



class SpellPluginManager:

    def __init__(self):
        self.pm = pluggy.PluginManager(PLUGIN_NAMESPACE)
        self.pm.add_hookspecs(SpellPluginSpec)

    def load_plugin(self, plugin: Any):
        self.pm.register(plugin)
        return self

    def load_plugin_from_module(self,
                                module_name: str,
                                hook_impl: type = SpellPluginImpl,
                                hook_spec=None):
        pass
