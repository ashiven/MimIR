from .._plugins.demo import demo as _demo

demo = _demo


def __getattr__(name):
    return getattr(_demo, name)


def __dir__():
    return sorted(set(globals()) | set(dir(_demo)))
