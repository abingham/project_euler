"""Simpler exercise runner.

Call it like: python run.py <exercise number>

This just runs the `main()` function in the exercise module.
"""

from importlib import import_module
import sys


def main(argv=None):
    if argv is None:
        argv = sys.argv
    ex = argv[1]
    mod = import_module('euler.euler_{}'.format(ex))
    print(mod.main())


if __name__ == '__main__':
    main()
