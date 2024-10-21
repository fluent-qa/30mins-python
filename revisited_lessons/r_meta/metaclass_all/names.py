class A:
    def func_a(self):
        pass


def func_a():
    pass


if __name__ == '__main__':
    print(func_a.__name__)
    print(func_a.__qualname__)
    print(A.__qualname__)
    print(A.__qualname__)
    print(A.func_a.__qualname__)
    print(A.func_a.__name__)
