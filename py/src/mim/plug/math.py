from .._plugins.math import math as _math

math = _math


def __getattr__(name):
    return getattr(_math, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_math)))
