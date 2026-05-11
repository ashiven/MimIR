from .._plugins.vec import vec as _vec

vec = _vec


def __getattr__(name):
    return getattr(_vec, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_vec)))
