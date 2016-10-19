# coding:utf8

try:
    import distribute_setup
    distribute_setup.use_setuptools()
except:
    pass
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='fn-compose',
    version='1.1.3',
    description='Make python support function compostion via the matmul operator',
    author='Ryan Kung',
    author_email='ryankung@ieee.org',
    package_dir={'': '.'},
    license='MIT',
    url='https://github.com/RyanKung/fn-compose.git',
    download_url='https://github.com/RyanKung/fn-compose/tarball/1.1.2/',
    long_description='''
    Make python support function compostion via the matmul operator

Compose

    >>> from compose import Compose
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
    ... 4

Compose and Currying

    >>> from compose.operator import *
    >>> add % 3
    ... partial(add, 3)
    >>> (add%3@add)(1, 2)
    ... 6

Pipe adn Stream

    >>> [1, 2, 3] | (a@b@c)
    ... map(a@b@c, [4, 5, 6])

    >>> (a@b@c) << [1, 2, 3]
    ... map(a@b@c, [4, 5, 6])

   ''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        "Programming Language :: Python :: 3.5",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
