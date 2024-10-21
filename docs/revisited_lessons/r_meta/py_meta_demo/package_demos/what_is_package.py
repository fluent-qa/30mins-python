import inspect
import os


def use_package():
    return os.getcwd()


if __name__ == '__main__':
    print(use_package())
