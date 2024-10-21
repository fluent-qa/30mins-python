import pkgutil
from abc import ABC


class PluginInterface(ABC):
    def run(self):
        pass


class PluginHello(PluginInterface):
    def run(self):
        print('Hello from plugin!')


class PluginManager:
    def __init__(self):
        self.plugins = []

    def discover_plugins(self):
        for item in pkgutil.iter_modules():
            print(item)
        for _, name, _ in pkgutil.iter_modules():
            print(f'module_name in path:{name}')
            if name.startswith('plugin_'):
                print(name)
                # module = importlib.import_module(name)
                # plugin_class = getattr(module, 'Plugin')
                # plugin = plugin_class()
                # self.plugins.append(plugin)

    def run_plugins(self):
        for plugin in self.plugins:
            plugin.run()
