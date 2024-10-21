class MyDemoHandler:
    def __init__(self, fname, method):
        self.fname = fname
        self.method = method
        self.file_object = open(self.fname, method)

    def __enter__(self):
        print("enter")
        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit ")
        self.file_object.close()


with MyDemoHandler("test.txt", "w") as fn:
    print("in the with block")
    print("do something")

from contextlib import contextmanager


@contextmanager
def thisFunc(fname, method):
    print("This is the implicit ENTER block")
    my_file = open(fname, method)

    yield my_file

    print("This is the implicit EXIT block")
    my_file.close()


with thisFunc("this_file.txt", "w") as example:
    ######### read write statements #########
    print("I'm in WITH block")
    pass
