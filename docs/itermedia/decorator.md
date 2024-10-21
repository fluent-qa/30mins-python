# Decorator

allows a user to add new functionality to an existing object without modifying its structure.

But How?
```python
def first(msg):
    print(msg)


first("Hello")

second = first
second("Hello")
```

```python
def is_called():  # created 1st function
    def is_returned():  # Created 2nd function (nested)
        print("Hello")
    return is_returned


new = is_called()

# Outputs "Hello"
new()

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
# Normal function
@uppercase_decorator
def greeting():
    return 'Welcome to Python'

g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON
print(greeting())
@uppercase_decorator
def greeting_it():
    return 'Welcome to Python'

print(greeting_it())
```
## Decorate Arguments
```python
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide with 0")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

divide(1,2)
divide(1,0)

# Example:

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

def work_for_all(function):
    def wrapper_accepting_parameters(*args, **kwargs):
        function(*args,**kwargs)
        print("I live in {}".format(args[2]))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Milaan", "Parmar",'London')
```
## Chain Decorators
```python
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")
```

```python
'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
```
