def print_md(param, obj_var_base):
    print("# {} \n {}".format(param, obj_var_base))


class Base:
    # Class variables are shared between all instances of the class Base, and declared like this:
    base_class_var = "Base"

    # The object constructor/init method, Note the first 'self' argument, which refers to the object instance.
    def __init__(self):
        print("calling Base.__init__")
        # Object variables are specific to a given instance of Base
        # Each object has a builtin hash member: __dict__ this one lists all object members (including those added by the base class __init__ method)
        self.obj_var_base = 10

    # An object method - needs to access the object instance, which is passed as first 'self' argument.
    def show_base(self):
        print_md("obj_var_base: ", self.obj_var_base)

    # A class method/static method is called without an object instance.
    @staticmethod
    def make_base():
        return Base()


# class Foo with a base class Base
class Foo(Base):
    # Class variables are shared between all instances of the class Foo, and declared like this:
    class_var = 42
    class_var2 = 43

    # The object constructor/init method, Note the first 'self' argument, which is the object instance.
    def __init__(self):
        # When not calling the base class __init__ method: the base class object variables are not added  to the object !!!
        # The base class __init__ adds the 'obj_var_base' member to the __dict__ member of this object instance.
        # By convention: you first init the base classes, before initialising the derived class.
        super().__init__()

        print("calling Foo.__init__")

        # Object variables are specific to a given instance of Foo
        # Each object has a builtin hash member: __dict__ this one lists all object members (including those added by the base class __init__ method)

        # Define object variable: obj_var_a
        self.obj_var_a = 42

        # Define object variable: obj_var_b
        self.obj_var_b = "name"

    # An object method - needs to access the object instance, which is passed as first 'self' argument.
    def show_derived(self):
        print_md("obj_var_a:", self.obj_var_a, "obj_var_b:", self.obj_var_b)

    # A class method/static method is called without an object instance.
    @staticmethod
    def make_foo():
        return Foo()


# Make a new object instance of type Foo class.
foo_obj = Foo()

print(foo_obj)
print(Foo)
print("id(foo_obj) : ", id(foo_obj))
print("foo_obj.__dict__ : ", foo_obj.__dict__)
assert id(foo_obj.__dict__) == id( getattr(foo_obj,'__dict__',None) )
print("dir(foo_obj) : ", dir(foo_obj))

# how class type
print("class of object foo_obj - type(foo_obj): ", type(foo_obj))
print("foo_obj.__class__ and getattr(foo_obj,'__class__',None) is the same thing!")
assert id(foo_obj.__class__) == id( getattr(foo_obj,'__class__',None) )
print("foo_boj.__class__.__name__ : ", foo_obj.__class__.__name__)
print("foo_boj.__class__.__qualname__ : ", foo_obj.__class__.__qualname__)
print("foo_obj.__class__.__bases__ :", foo_obj.__class__.__bases__)
print("foo_obj.__class__.__mro__ :", foo_obj.__class__.__mro__)


