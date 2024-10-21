# args and kwargs

```python
def func_args(*args,**kwargs):
  print(args)
  print(type(args))
  print(kwargs)
  print(type(kwargs))
  for item in args:
    print(item)
  for item in kwargs:
    print(item,kwargs[item])

func_args(1,2,3,4,5,a=123,b=456)

```

```python

```
