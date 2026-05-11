from .._plugins.mem import mem as _mem

mem = _mem


def __getattr__(name):
    return getattr(_mem, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_mem)))
