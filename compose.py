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

    """
    def __init__(self, function):
        self.function = function

    def __matmul__(self, other):
        return Compose(lambda *args, **kwargs: self.function(other(*args, **kwargs)))

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
