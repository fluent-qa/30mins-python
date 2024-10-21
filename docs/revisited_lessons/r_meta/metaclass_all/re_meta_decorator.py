from __future__ import annotations


class MyMeta(type):
    def __init__(cls, name, bases, attrs):
        for name, attr in attrs.items():
            if hasattr(attr, 'my_decorator'):
                # Decorate the method with some additional functionality...
                decorated_method = attr.my_decorator(attr)
                setattr(cls, name, decorated_method)
        return super().__init__(name, bases, attrs)


def my_decorator(method):
    def decorated_method(self):
        # Add some additional functionality here...
        return method(self)

    decorated_method.my_decorator = True
    return decorated_method


class MyClass(metaclass=MyMeta):
    @my_decorator
    def my_method(self):
        pass
