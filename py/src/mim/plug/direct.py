from .._plugins.direct import direct as _direct

direct = _direct


def __getattr__(name):
    return getattr(_direct, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_direct)))
