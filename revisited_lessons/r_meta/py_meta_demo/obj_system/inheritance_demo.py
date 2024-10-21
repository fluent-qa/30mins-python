import inspect


def show_type_hierarchy(type_class):
    def show_type_hierarchy_imp(type_class, nesting):
        if len(type_class.__bases__) == 0:
            return

        prefix = "	" * nesting
        print(prefix + "type:", type_class.__name__, "base types:",
              ",".join(map(lambda ty: ty.__name__, type_class.__bases__)))
        # print( prefix + "str(",  type_class.__name__ , ").__dict__ : ",  type_class.__dict__ )
        for base in type_class.__bases__:
            show_type_hierarchy_imp(base, nesting + 1)

    if not inspect.isclass(type_class):
        print("object ", str(type_class), " is not class")
        return

    print("show type hierarchy of class:")
    show_type_hierarchy_imp(type_class, 0)


class LevelOneFirst:
    pass


class LevelOneSecond:
    pass


class LevelOneThird:
    pass


class LevelTwoFirst(LevelOneFirst, LevelOneSecond):
    pass


class LevelThree(LevelTwoFirst, LevelOneThird):
    pass


show_type_hierarchy(LevelThree)

print("LevelThree.__mro__:", LevelThree.__mro__)
t = LevelThree()

print("*** mro in detail:")
for cls in t.__class__.__mro__:
    print("	class-in-mro: ", str(cls), "id:", id(cls), "cls.__dict__: ", cls.__dict__)
print("*** eof mro in detail")
print("dir(foo_obj.__class__) : ", dir( t.__class__ ) )

assert isinstance(t.__class__, type)
# same thing as
assert inspect.isclass(t.__class__)

# an object is not derived from class type.
assert not isinstance(t, type)
# same thng as
assert not inspect.isclass(t)

print("inspect.getmembers(t): ", inspect.getmembers(t))
