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
    name='compose',
    version='1.0',
    description='',
    author='Ryan Kung',
    author_email='ryankung@ieee.org',
    py_modules=['compose'],
    license='MIT',
    url='https://github.com/RyanKung/compose.git',
    download_url='https://github.com/RyanKung/compose/tarball/master',
    long_description='''
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
    ''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Programming Language :: Python::3.5',
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
