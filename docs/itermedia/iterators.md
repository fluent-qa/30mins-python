
```python

```
# Iterators 

- How iterator works and how you can build your own iterator using ```__iter__``` and ```__next__``` methods

## Iterator Example
```python
# define a list
my_list = [6, 9, 0, 3]  # 4 elements

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

print(next(my_iter))       # Output: 6
print(next(my_iter))       # Output: 9

# next(obj) is same as obj.__next__()

print(my_iter.__next__())  # Output: 0
print(my_iter.__next__())  # Output: 3

# This will raise error, no items left
next(my_iter)
```
## For Loop for Iterator
```python
my_list = [6, 9, 0, 3]  # 4 elements
for item in my_list:
  print(item)

iter_obj = iter(my_list)
while True:
  try:
    element = next(iter_obj)
    print(element)
  except StopIteration as e:
    print("stop iteration")
    break
```
## Customer Iterator

- __iter__()
- __next__()
```python
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(4)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
```

```python
class InfIter:
  
  def __init__(self):
    pass
  
  def __iter__(self):
    self.num=1
    return self
  def __next__(self):
    num = self.num
    self.num += 2
    return num

a = iter(InfIter())
print(next(a))
print(next(a))
print(next(a))
print(next(a))
```
