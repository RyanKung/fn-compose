```
    Make python support function compostion with matrix_mul operator

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
```
