class MySlotClass:
    __slots__ = ('attr1', 'attr2')
    """
    define slot attributes
    """
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


class MyClass:
    # __slots__ = ('attr1', 'attr2')

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


setattr(MyClass(1, 2), "tmp", "test")
setattr(MySlotClass(1, 2), "tmp", "test")
