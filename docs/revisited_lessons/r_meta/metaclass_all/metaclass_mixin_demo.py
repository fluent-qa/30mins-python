from sqlmodel import SQLModel


class Meta(type):
    def __new__(cls, name, bases, attrs, greeting=SQLModel, **kwargs):
        print(f"创建类 {name}...")
        attrs['say_hello'] = lambda self: f"Hello from {name}! {kwargs.get('greeting', 'Welcome')}"
        return super().__new__(cls, name, bases, attrs)

    def __init__(self, name, bases, attrs, greeting=SQLModel, **kwargs):
        print(f"初始化类 {name}...")
        super().__init__(name, bases, attrs)
        self.base_type = greeting


class MyClass(metaclass=Meta, greeting='Greetings'):
    def __init__(self, name):
        self.name = name
        print(f"初始化 MyClass 实例: {self.name}")
        self.base_type = name

    def my_method(self):
        print(f"调用 MyClass 的 my_method() 方法")


class MySubClass(MyClass, metaclass=Meta, greeting='Hola'):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print(f"初始化 MySubClass 实例: {self.name}, {self.age} 岁")

    def sub_method(self):
        print(f"调用 MySubClass 的 sub_method() 方法")


class MySubClassNoMeta(MyClass, greeting='MySubClassNoMeta'):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print(f"初始化 MySubClassNoMeta 实例: {self.name}, {self.age} 岁")
        self.base_type = age

    def sub_method(self):
        print(f"调用 MySubClassNoMeta 的 sub_method() 方法")


my_instance = MyClass("Alice")
my_instance.say_hello()
my_instance.my_method()

sub_instance = MySubClass("Bob", 25)
sub_instance.say_hello()
sub_instance.my_method()
sub_instance.sub_method()
print("base_type", sub_instance.base_type)

sub_no_meta_instance = MySubClassNoMeta("No-Meta", 25)
sub_no_meta_instance.sub_method()
print("base_type", sub_no_meta_instance.base_type)
print(getattr(sub_no_meta_instance, 'base_type'))
print(setattr(sub_no_meta_instance, 'base_type', 100))
print(getattr(sub_no_meta_instance, 'base_type'))


class MySubClassNoGreeting(MyClass):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print(f"初始化 MySubClassNoGreeting 实例: {self.name}, {self.age} 岁")

    def sub_method(self):
        print(f"调用 MySubClassNoGreeting 的 sub_method() 方法,{self.base_type}")


MySubClassNoGreeting('no-greeting', 100).sub_method()
