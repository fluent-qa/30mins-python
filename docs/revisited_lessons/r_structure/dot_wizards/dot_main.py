from revisited.r_data.dot_wizards.base import __add_repr__, __convert_to_dict__, __resolve_value__


def __setitem_impl__(self, key, value, __set=dict.__setitem__):
    """Implementation of `DotWiz.__setitem__` to preserve dot access"""
    value = __resolve_value__(value, DotAccessor)

    __set(self, key, value)
    self.__dict__[key] = value


def make_dot_wiz(*args, **kwargs):
    """
    Helper function to create and return a :class:`DotWiz` (dot-access dict)
    from an optional *iterable* object and *keyword* arguments.

    Example::

        >>> make_dot_wiz([('k1', 11), ('k2', [{'a': 'b'}]), ('k3', 'v3')], y=True)
        ✫(y=True, k1=11, k2=[✫(a='b')], k3='v3')

    """
    kwargs.update(*args)

    return DotAccessor(kwargs)


# noinspection PyDefaultArgument
def __upsert_into_dot_accessor__(self, input_dict={},
                                 __set=dict.__setitem__,
                                 **kwargs):
    """
    Helper method to generate / update a :class:`DotWiz` (dot-access dict)
    from a Python ``dict`` object, and optional *keyword arguments*.

    """
    __dict = self.__dict__

    if kwargs:
        # avoids the potential pitfall of a "mutable default argument" -
        # only update or modify `input_dict` if the param is passed in.
        if input_dict:
            input_dict.update(kwargs)
        else:
            input_dict = kwargs

    for key in input_dict:
        # note: this logic is the same as `__resolve_value__()`
        #
        # *however*, I decided to inline it because it's actually faster
        # to eliminate a function call here.
        value = input_dict[key]
        t = type(value)

        if t is dict:
            value = DotAccessor(value)
        elif t is list:
            value = [__resolve_value__(e, DotAccessor) for e in value]

        # note: this logic is the same as `DotWiz.__setitem__()`
        __set(self, key, value)
        __dict[key] = value


class DotAccessor(dict, metaclass=__add_repr__, print_char="*"):
    __slots__ = ("__dict__",)
    __init__ = update = __upsert_into_dot_accessor__
    __delattr__ = __delitem__ = dict.__delitem__
    __setattr__ = __setitem__ = __setitem_impl__

    def __getitem__(self, key):
        return self.__dict__[key]

    to_dict = __convert_to_dict__
    to_dict.__doc__ = 'Recursively convert the :class:`DotWiz` instance ' \
                      'back to a ``dict``.'
