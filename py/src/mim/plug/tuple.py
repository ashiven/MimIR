from .._plugins.tuple import tuple as _tuple

tuple = _tuple


def __getattr__(name):
    return getattr(_tuple, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_tuple)))
