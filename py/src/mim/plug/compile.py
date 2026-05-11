from .._plugins.compile import compile as _compile

compile = _compile


def __getattr__(name):
    return getattr(_compile, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_compile)))
