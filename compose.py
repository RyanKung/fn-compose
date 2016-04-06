from typing import Iterable, Callable


class Compose:
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
    def __init__(self, fn: Callable):
        self.fn = fn

    def __matmul__(self, fn: Callable):
        return Compose(lambda *args, **kwargs: self.fn(fn(*args, **kwargs)))

    def __ror__(self, xs: Iterable):
        return map(self.fn, xs)

    def __lshift__(self, xs: Iterable):
        return map(self.fn, xs)

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
