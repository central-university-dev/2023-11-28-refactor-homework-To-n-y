import foo
from . import foo


def foo(func):
    func = 'qwerty'


a = foo
a = foo()
print(foo)
print(foo())
