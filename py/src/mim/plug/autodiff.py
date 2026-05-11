from .._plugins.autodiff import autodiff as _autodiff

autodiff = _autodiff


def __getattr__(name):
    return getattr(_autodiff, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_autodiff)))
