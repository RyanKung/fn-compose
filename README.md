### Make python support function compostion via the matmul operator


#### Compose

```
    from compose import Compose
    
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
### Compose and Currying

```
    from compose.operator import *
    >>> add % 3
    partial(add, 3)
    
    >>> (add%3@add)(1, 2)
    6
```


### Pipe / Stream
```
    >>> [1, 2, 3] | (a@b@c)
    map(a@b@c, [4, 5, 6])

    >>> (a@b@c) << [1, 2, 3]
    map(a@b@c, [4, 5, 6])

```
