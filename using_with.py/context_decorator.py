# in Python3 we have a context manager

from contextlib import contextmanager
import sys


@contextmanager
def outputRedirect(newOutput):
    old_std = sys.stdout
    sys.stdout = newOutput
    yield # our function will yield the next available content to be written
    sys.stdout = old_std


def main():
    print('using normal context')
    with open('my_log.txt', 'at') as fobj:
        with outputRedirect(fobj):
            print('redirected content')


if __name__ == '__main__':
    main()
