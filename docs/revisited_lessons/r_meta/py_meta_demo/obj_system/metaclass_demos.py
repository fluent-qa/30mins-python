class Singleton_metaclass(type):

    # invoked to create the class object instance (for holding static data)
    # this function is called exactly once, in order to create the class instance!
    def __new__(meta_class, name, bases, cls_dict, **kwargs):
        print("Singleton_metaclass: __new__ meta_class:", meta_class, "name:", name, "bases:", bases, "cls_dict:",
              cls_dict, f'kwargs: {kwargs}')

        class_instance = super().__new__(meta_class, name, bases, cls_dict)
        print("Singleton_metaclass: __new__ return value: ", class_instance, "type(class_instance):",
              type(class_instance))

        # the class class variable __singleton_instance__ will hold a reference to the one an only object instance of this class.
        class_instance.__singleton_instance__ = None

        return class_instance

    def __call__(cls, *args, **kwargs):
        # we get here to create an object instance. the class object has already been created.
        print("Singleton_metaclass: __call__ args:", *args, f'kwargs: {kwargs}')

        # check if the singleton has already been created.
        if cls.__singleton_instance__ is None:
            # create the one an only instance object.
            instance = cls.__new__(cls)

            # initialise the one and only instance object
            instance.__init__(*args, **kwargs)

            # store the singleton instance object in the class variable __singleton_instance__
            cls.__singleton_instance__ = instance

        # return the singleton instance
        return cls.__singleton_instance__


import math


# the metaclass specifier tells python to use the Singleton_metaclass, for the creation of an instance of type SquareRootOfTwo
class SquareRootOfTwo(metaclass=Singleton_metaclass):

    # the __init__ method is called exactly once, when the first instance of the singleton is created.
    # the square root of two is computed exactly once.
    def __init__(self):
        self.value = math.sqrt(2)
        print("SquareRootOfTwo.__init__  self:", self)


print("creating the objects instances...")

sqrt_root_two_a = SquareRootOfTwo()
print("sqrt_two_a id(sqrt_root_two_a):", id(sqrt_root_two_a), "type(sqrt_root_two_a):", type(sqrt_root_two_a),
      "sqrt_root_two_a.value:", sqrt_root_two_a.value)

sqrt_root_two_b = SquareRootOfTwo()

print("sqrt_two_b id(sqrt_root_two_b)", id(sqrt_root_two_b), "type(sqrt_root_two_b):", type(sqrt_root_two_b),
      "sqrt_root_two_b.value:", sqrt_root_two_b.value)

# all singleton objects of the same class are referring to the same object
assert id(sqrt_root_two_a) == id(sqrt_root_two_b)

import enum


class Rainbow(enum.Enum):
    RED = 1
    ORANGE = 2
    YELLOW = 3
    GREEN = 4
    BLUE = 5
    INDIGO = 6
    VIOLET = 7


color = Rainbow.GREEN

print("type(Rainbow.GREEN):", type(Rainbow.GREEN))
print("The string rep Rainbow.Green.name:", Rainbow.GREEN.name, "type(Rainbow.GREEN.name):", type(Rainbow.GREEN.name))
print("The integer rep Rainbow.GREEN.value: ", Rainbow.GREEN.value, "type(Rainbow.GREEN.value):",
      type(Rainbow.GREEN.value))
print("Access by name: Rainbow['GREEN']:", Rainbow['GREEN'])
print("Access by value: Rainbow(4):", Rainbow(4))

# which is the same thing
assert id(Rainbow['GREEN']) == id(Rainbow(4))


class Singleton_metaclass_with_args(type):

    # invoked to create the class object instance (for holding static data)
    # this function is called exactly once, in order to create the class instance!
    def __new__(meta_class, name, bases, cls_dict, **kwargs):
        print("Singleton_metaclass_with_args: __new__ meta_class:", meta_class, "name:", name, "bases:", bases,
              "cls_dict:", cls_dict, f'kwargs: {kwargs}')

        class_instance = super().__new__(meta_class, name, bases, cls_dict)
        print("Singleton_metaclass_with_args: __new__ return value: ", class_instance, "type(class_instance):",
              type(class_instance))

        # the class class variable __singleton_instance__ will hold a reference to the one an only object instance of this class.
        class_instance.__singleton_instance__ = None

        # the keywords that have been specified, are passed into the class creation method __new__.
        # save them as a class variable, so as to pass them to the object constructor!
        class_instance.__kwargs__ = kwargs

        return class_instance

    def __call__(cls, *args, **kwargs):
        # we get here to create an object instance. the class object has already been created.
        print("Singleton_metaclass_with_args: __call__ args:", *args, f'kwargs: {kwargs}')

        # check if the singleton has already been created.
        if cls.__singleton_instance__ is None:
            # create the one an only instance object.
            instance = cls.__new__(cls)

            # initialise the one and only instance object
            # pass it the keyword parameters specified for the class!
            instance.__init__(*args, **cls.__kwargs__)

            # store the singleton instance object in the class variable __singleton_instance__
            cls.__singleton_instance__ = instance

        # return the singleton instance
        return cls.__singleton_instance__


import math


class AnySquareRoot:
    def __init__(self, arg_val):
        self.value = math.sqrt(arg_val)


# the metaclass specifier tells python to use the Singleton_metaclass, for the creation of an instance of type SquareRootOfTwo
class SquareRootOfTwo(AnySquareRoot, metaclass=Singleton_metaclass_with_args, arg_num=2):
    # the init method is called with arg_num specified in the class definition (value of 2)
    def __init__(self, arg_num):
        super().__init__(arg_num)


class SquareRootOfThree(AnySquareRoot, metaclass=Singleton_metaclass_with_args, arg_num=3):
    # the init method is called with arg_num specified in the class definition (value of 3)
    def __init__(self, arg_num):
        super().__init__(arg_num)


print("creating the objects instances...")

sqrt_root_two_a = SquareRootOfTwo()
print("sqrt_two_a id(sqrt_root_two_a):", id(sqrt_root_two_a), "type(sqrt_root_two_a):", type(sqrt_root_two_a),
      "sqrt_root_two_a.value:", sqrt_root_two_a.value)

sqrt_root_two_b = SquareRootOfTwo()
print("sqrt_two_b id(sqrt_root_two_b)", id(sqrt_root_two_b), "type(sqrt_root_two_b):", type(sqrt_root_two_b),
      "sqrt_root_two_b.value:", sqrt_root_two_b.value)

# all singleton objects of the same class are referring to the same object
assert id(sqrt_root_two_a) == id(sqrt_root_two_b)

sqrt_root_three_a = SquareRootOfThree()
print("sqrt_three_a id(sqrt_root_three_a):", id(sqrt_root_three_a), "type(sqrt_root_three_a):", type(sqrt_root_three_a),
      "sqrt_root_three_a.value:", sqrt_root_three_a.value)

sqrt_root_three_b = SquareRootOfThree()
print("sqrt_three_b id(sqrt_root_three_b)", id(sqrt_root_three_b), "type(sqrt_root_three_b):", type(sqrt_root_three_b),
      "sqrt_root_three_b.value:", sqrt_root_three_b.value)

# all singleton objects of the same class are referring to the same object
assert id(sqrt_root_three_a) == id(sqrt_root_three_b)

## https://github.com/MoserMichael/python-obj-system.git
