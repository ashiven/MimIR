from .._plugins.tensor import tensor as _tensor

tensor = _tensor


def __getattr__(name):
    return getattr(_tensor, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_tensor)))
