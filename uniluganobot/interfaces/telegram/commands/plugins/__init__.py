from pathlib import Path
import importlib

for module_file in (Path(__path__[0])).glob('*command.py'):
    module = '.' + module_file.name[:-3]
    importlib.import_module(module, __name__)
