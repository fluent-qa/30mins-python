def dispatcher(func):
    registry = {}

    def decorated(*args, **kwargs):
        print(args)
        key = args[0] if len(args) > 0 else func.__name__
        if key in registry:
            return registry[key](*args, **kwargs)
        else:
            register(key,func)
            return func(*args, **kwargs)

    def register(key, value):
        registry[key] = value

    decorated.register = register
    return decorated


@dispatcher
def func_1():
    print("in func_1")
    return "function_1"


if __name__ == '__main__':
    print(func_1())
