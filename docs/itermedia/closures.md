# Closures

High Order Functions: What is it?
- A function can take one or more functions as parameters
- A function can be returned as a result of another function
- A function can be modified
- A function can be assigned to a variable## Function as Parameter
```python
def sum_number(nums):
  return sum(nums)

def high_order_func(f,lst):
  result = f(lst)
  return result

sum_result = high_order_func(sum_number, [1,2,3,4,5,6,7,8,9])
print(sum_result)

## pass function and function parameter as input to do computation
```
## Function s Return Value
```python
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```
## No Local Parameter
```python
def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    printer()

# We execute the function
# Output: Hello
print_msg("Hello")
```

```python
def print_msg_func(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg_func("Hello") ## function could be determined by other conditions
another()
```
## Closure 好处

- 隐藏全局变量
```python
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result.__closure__[0].cell_contents)
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```
## map()/filter()

- map(): do something for every item and return to origin 
- filter(): filter something

## map()
```python
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```
## filter()
```python

numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num): 
    """
    Returns True if num is even, False otherwise.
    :param num: 
    :return: 
    """
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

names = ['Milaan', 'Arthur', 'Bill', 'Clark']  # iterable
def is_name_long(name):
    """
    Returns True if name is long, False otherwise.
    :param name: 
    :return: 
    """
    if len(name) > 5:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Milaan', 'Arthur']
```
