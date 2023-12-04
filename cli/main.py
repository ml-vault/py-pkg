import sys
from .data import main as data
from .config.main import config

NAMESPACES = ["data", "config"]

def main():
    input_args = sys.argv[1:]
    namespace_name, *args = input_args
    if namespace_name not in NAMESPACES:
        print(f"Namespace {namespace_name} not found")
        exit(1)
    if namespace_name == "data":
        data(args)
    elif namespace_name == "config":
        config()
        pass
