from contextlib import contextmanager

@contextmanager
def book1():
    print('<',end='')
    yield
    print('>',end='')

with book1():
    print('xfz',end='')