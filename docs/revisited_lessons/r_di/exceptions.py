import inspect
import itertools
import sys
import types
from typing import Optional, NoReturn, cast

from .utils import describe


class InjectError(Exception):
    """Base exception."""


class UnsatisfiedRequirement(InjectError):
    """Requirement could not be satisfied."""

    def __init__(self, owner: Optional[object], interface: type) -> None:
        super().__init__(owner, interface)
        self.owner = owner
        self.interface = interface

    def __str__(self) -> str:
        on = '%s has an ' % describe(self.owner) if self.owner else ''
        return '%sunsatisfied requirement on %s' % (on, describe(self.interface))


class CallError(InjectError):
    """Call to callable object fails."""

    def __str__(self) -> str:
        if len(self.args) == 1:
            return self.args[0]

        instance, method, args, kwargs, original_error, stack = self.args
        cls = instance.__class__.__name__ if instance is not None else ''

        full_method = '.'.join((cls, method.__name__)).strip('.')

        parameters = ', '.join(
            itertools.chain(
                (repr(arg) for arg in args), ('%s=%r' % (key, value) for (key, value) in kwargs.items())
            )
        )
        return 'Call to %s(%s) failed: %s (injection stack: %r)' % (
            full_method,
            parameters,
            original_error,
            [level[0] for level in stack],
        )


class CircularDependency(InjectError):
    """Circular dependency detected."""


class UnknownProvider(InjectError):
    """Tried to bind to a type whose provider couldn't be determined."""


class UnknownArgument(InjectError):
    """Tried to mark an unknown argument as noninjectable."""


def reraise(original: Exception, exception: Exception, maximum_frames: int = 1) -> NoReturn:
    prev_cls, prev, tb = sys.exc_info()
    frames = inspect.getinnerframes(cast(types.TracebackType, tb))
    if len(frames) > maximum_frames:
        exception = original
    raise exception.with_traceback(tb)
