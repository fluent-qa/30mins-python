import inspect
from typing import TypeVar

from rich import print
from functools import wraps


def trace_basic(func):
    def wrapper():
        func_name = func.__name__
        print(f'Entering "{func_name}" function')
        func()
        print(f'Exiting from "{func_name}" function')

    return wrapper


def say_hello():
    print('Hello!')


say_hello = trace_basic(say_hello)
say_hello()


def trace(func):
    print("the context is ", func)
    print("the context is ", inspect.getsource(func))
    parameters = inspect.getfullargspec(func)
    print("the context is ", parameters)

    def wrapper(*args, **kwargs):
        print("decorated target is", func.__name__)
        func_name = func.__name__
        print(f'Entering "{func_name}" function')
        result = func(*args, **kwargs)
        print(f'Result of "{func_name}" function is {result}')
        print(f'Exiting from "{func_name}" function')
        return result

    return wrapper


def trace_better(func):
    @wraps(func)
    def wrapper():
        func_name = func.__name__
        print(f'Entering "{func_name}" function')
        result = func()
        print(f'Result of "{func_name}" function is {result}')
        print(f'Exiting from "{func_name}" function')
        return result

    return wrapper


@trace
def say_hello():
    return 'Hello!'


@trace_better
def say_hello_new():
    return 'Hello!'


@trace
def say_with_args(name):
    return 'Hello {}'.format(name)


func_result = say_hello()
print("the final result is ", func_result)

func_result = say_with_args("name")
print("the final result is ", func_result)

## 问题:
# 1. 装饰了谁
# 2. 上下文如何传递: 函数的参数怎么传

from functools import wraps


## nested
def multiply_by(multiplier):
    def decorator(func):
        @wraps(func)
        def deco(*args, **kwargs):
            func_name = func.__name__
            print(f'Calling "{func_name}({args[0]}, {args[1]})" function')
            print(f'"{func_name}" function is multiplied by {multiplier}')
            result = func(*args, **kwargs) * multiplier
            print(f'Result equals to {result}')
            return result

        return deco

    return decorator


@multiply_by(multiplier=3)
@multiply_by(multiplier=4)  ## nested
def add(a, b):
    return a + b


add(2, 3)

T = TypeVar("T")


def private(something: T):
    print(something)
    something.__private__ = True
    return something


def simple_method():
    print("Hello World")


@private
def simple_method_1():
    print("Hello World-1")


private(simple_method)()
simple_method_1()
