import pluggy

from revisited.r_plugin_pattern.plugins import PLUGIN_NAMESPACE

spell_hook_spec = pluggy.HookspecMarker(PLUGIN_NAMESPACE)
spell_hook_impl = pluggy.HookimplMarker(PLUGIN_NAMESPACE)


class SpellPluginImpl:
    pass


class SpellPluginSpec:

    @spell_hook_spec
    def pre_invoke(self, **input):
        pass

    @spell_hook_spec
    def invoke(self, **input):
        pass

    @spell_hook_spec
    def after_invoke(self, **input):
        pass
