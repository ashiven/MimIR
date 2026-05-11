from .._plugins.matrix import matrix as _matrix

matrix = _matrix


def __getattr__(name):
    return getattr(_matrix, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_matrix)))
