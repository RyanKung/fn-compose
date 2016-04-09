from typing import Iterable, Callable, Any
from functools import partial


class Compose(object):
    """
    Make python support function compostion

    >>> @Compose
    ... def a(x):
    ...     return x

    >>> @Compose
    ... def b(x):
    ...     return x + 1

    >>> @Compose
    ... def c(x):
    ...     return x + 2

    >>> (a@b@c)(1)
    4

    >>> list([1, 2, 3] | (a@b@c))
    [4, 5, 6]

    >>> list((a@b@c) << [1, 2, 3])
    [4, 5, 6]


    """
    @staticmethod
    def compose(fn0, fn1):
        return lambda *args, **kwargs: fn0(fn1(*args, **kwargs))

    def __init__(self, fn: Callable) -> Callable:
        self.fn = fn

    def __mod__(self, value) -> Callable:
        return Compose(partial(self.fn, value))

    def __matmul__(self, fn: Callable) -> Callable:
        return Compose(self.compose(self.fn, fn))

    def __ror__(self, xs: Iterable) -> Iterable:
        return map(self.fn, xs)

    def __lshift__(self, xs: Iterable) -> Iterable:
        return map(self.fn, xs)

    def __call__(self, *args, **kwargs) -> Any:
        return self.fn(*args, **kwargs)
