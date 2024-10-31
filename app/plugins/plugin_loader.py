import os
import importlib
from app.plugins.plugin import Plugin

def load_plugins():
    plugins = []
    plugin_dir = os.path.dirname(__file__)

    for entry in os.listdir(plugin_dir):
        path = os.path.join(plugin_dir, entry)
        if os.path.isdir(path):  
            module_name = entry
            module = importlib.import_module(f"app.plugins.{module_name}")

            for name in dir(module):
                obj = getattr(module, name)
                if isinstance(obj, type) and issubclass(obj, Plugin) and obj is not Plugin:
                    plugins.append(obj())  

        elif entry.endswith(".py") and entry != "__init__.py":
            module_name = entry[:-3] 
            module = importlib.import_module(f"app.plugins.{module_name}")

            for name in dir(module):
                obj = getattr(module, name)
                if isinstance(obj, type) and issubclass(obj, Plugin) and obj is not Plugin:
                    plugins.append(obj())  

    return plugins
