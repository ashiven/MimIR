from .._plugins.option import option as _option

option = _option


def __getattr__(name):
    return getattr(_option, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_option)))
