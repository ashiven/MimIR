from .._plugins.gpu import gpu as _gpu

gpu = _gpu


def __getattr__(name):
    return getattr(_gpu, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_gpu)))
