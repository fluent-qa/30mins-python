
# import required modules
import inspect
import numpy

# use ismodule()
print(inspect.ismodule(numpy))


# create class
class A(object):
    pass


# use isclass()
print(inspect.isclass(A))


def inspect_module(module_name:str):
    return inspect.getmodule(module_name)


module_name = "pyqa_30min.metaclass_all.reflections.module_demo"
module = __import__(module_name)
print(module)

if __name__ == '__main__':
    inspect_module("test")
