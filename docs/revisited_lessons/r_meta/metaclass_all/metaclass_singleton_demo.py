from abc import ABCMeta


class SingletonMeta(ABCMeta):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class DatabaseClient(metaclass=SingletonMeta):
    pass


d1 = DatabaseClient()
d2 = DatabaseClient()

print(d1 == d2)


class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"正在创建类 {name}...")
        attrs['my_method'] = lambda self: f"来自 {name} 的方法"
        return super().__new__(cls, name, bases, attrs)


class BaseClass:
    def __init__(self, config):
        self.config = config

    def say_hello(self):
        print("你好，来自 BaseClass!")


class BaseClassClient(BaseClass):
    def __init__(self, config=None):
        if config is None:
            self.config="default"
        super().__init__(self.config)


class SubClass(BaseClassClient, metaclass=MyMeta):
    def sub_method(self):
        print("sub_method")


# 创建 SubClass 对象
sub_obj = SubClass()

# 使用 SubClass 对象调用 BaseClass 中的 say_hello 方法
sub_obj.say_hello()  # 输出：你好，来自 BaseClass!

# 使用 SubClass 对象调用 MyMeta 元类添加的 my_method 方法
print(sub_obj.my_method())  # 输出：来自 SubClass 的方法
sub_obj.sub_method()


