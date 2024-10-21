from typing import Generic, TypeVar, Type, Callable, Annotated

inject_marker = object()
noinject_marker = object()

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')
CallableT = TypeVar('CallableT', bound=Callable)
InjectT = TypeVar('InjectT')
Inject = Annotated[InjectT, inject_marker]
NoInject = Annotated[InjectT, noinject_marker]
