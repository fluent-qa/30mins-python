from revisited.r_data.dot_wizards.dot_main import DotAccessor
from revisited.r_data.dot_wizards.dot_plus import DotWizPlus
## https://github.com/rnag/dotwiz.git

def __add_repr__(name, bases, cls_dict, *, print_char='*', use_attr_dict=False):
    """
    Metaclass to generate and add a `__repr__` to a class.
    """

    # if `use_attr_dict` is true, use attributes defined in the instance's
    # `__dict__` instead.
    if use_attr_dict:
        def __repr__(self: dict):
            fields = [f'{k}={v!r}' for k, v in self.__dict__.items()]
            return f'{print_char}({", ".join(fields)})'

    else:
        def __repr__(self: dict, items_fn=dict.items):
            # noinspection PyArgumentList
            fields = [f'{k}={v!r}' for k, v in items_fn(self)]
            return f'{print_char}({", ".join(fields)})'

    cls_dict['__repr__'] = __repr__

    return type(name, bases, cls_dict)


def __convert_to_attr_dict__(o):
    """
    Recursively convert an object (typically a `dict` subclass) to a
    Python `dict` type, while preserving the lower-cased keys used
    for attribute access.
    """
    if isinstance(o, dict):
        return {k: __convert_to_attr_dict__(v) for k, v in o.__dict__.items()}

    if isinstance(o, list):
        return [__convert_to_attr_dict__(e) for e in o]

    return o


def __convert_to_dict__(o, __items_fn=dict.items):
    """
    Recursively convert an object (typically a `dict` subclass) to a
    Python `dict` type.
    """
    if isinstance(o, dict):
        # use `dict.items(o)` instead of `o.items()`, to work around this issue:
        #   https://github.com/rnag/dotwiz/issues/4
        return {k: __convert_to_dict__(v) for k, v in __items_fn(o)}

    if isinstance(o, list):
        return [__convert_to_dict__(e) for e in o]

    return o


def __resolve_value__(value, dict_type):
    """Resolve `value`, which can be a complex type like `dict` or `list`"""
    t = type(value)

    if t is dict:
        value = dict_type(value)

    elif t is list:
        value = [__resolve_value__(e, dict_type) for e in value]

    return value


def set_default_for_missing_keys(default=None, overwrite=False):
    """
    Modifies :class:`DotWiz` and :class:`DotWizPlus` to add a custom
    :meth:`__getattr__`, so that accessing missing or non-existing attributes
    (keys) returns ``default`` instead of raising an :exc:`AttributeError`.

    This provides a handy alternative to the builtin :func:`hasattr`.

    For more details, see https://github.com/rnag/dotwiz/issues/14.

    Example::

        >>> from dotwiz import DotWiz, set_default_for_missing_keys
        >>> set_default_for_missing_keys('test')
        >>> dw = DotWiz(hello='world!')
        >>> assert dw.hello == 'world!'
        >>> assert dw.world == 'test'

    :param default: The default value to return for missing or non-existing
      attributes (keys).
    :param overwrite: True to overwrite a class's `__getattr__()` method,
      if one already exists; defaults to False.

    """
    for cls in DotAccessor, DotWizPlus:
        cls_dict = cls.__dict__

        if not overwrite and '__getattr__' in cls_dict:
            msg = f'{cls.__qualname__} already defines a __getattr__() - ' \
                  f'pass `overwrite=True` to continue anyway.'
            raise ValueError(msg)

        def __getattr__(self: cls, item: str,
                        __default=default,
                        __get=cls_dict.get):

            return __get(item, __default)

        setattr(cls, '__getattr__', __getattr__)
