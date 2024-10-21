# https://medium.com/@miguel.amezola/demystifying-python-metaclasses-understanding-and-harnessing-the-power-of-custom-class-creation-d7dff7b68de8
class SimpleMeta(type):
    def __new__(cls, name, bases, attrs, *args, **kwargs):  ## name, attrs
        print(f"Creating class: {name}")
        print(f"Creating class from bases: {bases}")
        print(f"Creating class from attrs: {attrs}")
        print(f"Creating class from args: {args}")
        print(f"Creating class from kwags: {kwargs}")
        return super().__new__(cls, name, bases, attrs, *args, **kwargs)

    def __init__(cls, name, bases, attrs, *args, **kwargs):
        super().__init__(name, bases, attrs, *args, **kwargs)


class SimpleClass(metaclass=SimpleMeta):
    pass


print(SimpleClass())


## Use cases:
## 1. Adding additional methods or attributes to classes
## 2. Enforcing constraints on the creation of classes

class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['new_attribute'] = 'Hello, World!'
        attrs['new_method'] = lambda self: 'Hello from a new method!'
        if 'required_attribute' not in attrs:
            raise TypeError('Class must define required_attribute')
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=MyMeta):
    required_attribute = 'Hello, World!'


# class MyInvalidMetaclass(metaclass=MyMeta):
#     pass


print(MyClass().new_attribute)
MyClass().new_method()


# MyInvalidMetaclass()

## 3. Implementing domain-specific languages (DSLs)
# class DomainSpecificLanguage(type):
#     def __new__(cls, name, bases, attrs):
#         # Find all methods starting with "when_" and store them in a dictionary
#         events = {k: v for k, v in attrs.items() if k.startswith("when_")}
#         print(events)
#         # Create a new class that will be returned by this metaclass
#         new_cls = super().__new__(cls, name, bases, attrs)
#
#         # Define a new method that will be added to the class
#         def listen(self, event):
#             if event in events:
#                 events[event](self)
#
#         # Add the new method to the class
#         new_cls.listen = listen
#
#         return new_cls


# # Define a class using the DSL syntax,not valid case
# class MyDSLClass(metaclass=DomainSpecificLanguage):
#     def when_hello(self):
#         return ("Hello!")
#
#     def when_goodbye(self):
#         return ("Goodbye!")
#
#
# # Use the DSL syntax to listen for events
# obj = MyDSLClass()
# print(obj.listen("hello"))  # Output: "Hello!"
# print(obj.listen("goodbye"))  # Output: "Goodbye!"
# # print(obj.events)

