from .._plugins.ord import ord as _ord

ord = _ord


def __getattr__(name):
    return getattr(_ord, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_ord)))
