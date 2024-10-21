import functools
import inspect
import logging
import os
import threading
from typing import Any, cast, Callable, Union, AnyStr

from revisited.r_di.types import T, CallableT

log = logging.getLogger('injector')
log.addHandler(logging.NullHandler())
if log.level == logging.NOTSET:
    log.setLevel(logging.WARN)


def private(something: T) -> T:
    something.__private__ = True  # type: ignore
    return something


def describe(c: Any) -> str:
    if hasattr(c, '__name__'):
        return cast(str, c.__name__)
    if type(c) in (tuple, list):
        return '[%s]' % c[0].__name__
    return str(c)


def synchronized(lock: threading.RLock) -> Callable[[CallableT], CallableT]:
    def outside_wrapper(function: CallableT) -> CallableT:
        @functools.wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            with lock:
                return function(*args, **kwargs)

        return cast(CallableT, wrapper)

    return outside_wrapper


lock = threading.RLock()


def get_dependency_name(dependency: Union[type, callable, str]) -> str:
    if isinstance(dependency, str):
        return dependency
    return dependency.__qualname__


def get_caller_filepath(steps_back: int = 2) -> AnyStr:
    """
    Utility function to get the caller's filepath using inspection.

    :param steps_back: (optional) 1 step back in the call stack would return the file of
        the caller of this function. Defaults to 2, i.e. the path of the file of the
        caller of this function's caller.
    """
    frame_info = inspect.stack()[steps_back]
    filepath = frame_info.filename
    del frame_info
    return os.path.abspath(filepath)
