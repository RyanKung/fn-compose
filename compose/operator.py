import operator
from compose import Compose
import sys

__doc__ = '''
>>> (add%3@add)(1, 2)
6
>>> add(1, 2)
3
>>> (add % 1)(2)
3
'''

__all__ = operator.__all__
sys.modules[__name__].__dict__.update(
    {op: Compose(getattr(operator, op))
     for op in operator.__all__})
