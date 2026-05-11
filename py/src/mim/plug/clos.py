from .._plugins.clos import clos as _clos

clos = _clos


def __getattr__(name):
    return getattr(_clos, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_clos)))
