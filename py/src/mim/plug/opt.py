from .._plugins.opt import opt as _opt

opt = _opt


def __getattr__(name):
    return getattr(_opt, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_opt)))
