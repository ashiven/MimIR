from .._plugins.affine import affine as _affine

affine = _affine


def __getattr__(name):
    return getattr(_affine, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_affine)))
