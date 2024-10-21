import abc
from typing import Generic, Type, Callable, List, Dict

from .types import T
from .utils import private


class Provider(Generic[T]):
    """Provides class instances."""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get(self, injector: 'Injector') -> T:
        raise NotImplementedError  # pragma: no cover


class ClassProvider(Provider, Generic[T]):
    """Provides instances from a given class, created using an Injector."""

    def __init__(self, cls: Type[T]) -> None:
        self._cls = cls

    def get(self, injector: 'Injector') -> T:
        return injector.create_object(self._cls)


class CallableProvider(Provider, Generic[T]):
    """Provides something using a callable.

    The callable is called every time new value is requested from the provider.

    There's no need to explicitly use :func:`inject` or :data:`Inject` with the callable as it's
    assumed that, if the callable has annotated parameters, they're meant to be provided
    automatically. It wouldn't make sense any other way, as there's no mechanism to provide
    parameters to the callable at a later time, so either they'll be injected or there'll be
    a `CallError`.

    ::

        >>> class MyClass:
        ...     def __init__(self, value: int) -> None:
        ...         self.value = value
        ...
        >>> def factory():
        ...     print('providing')
        ...     return MyClass(42)
        ...
        >>> def configure(binder):
        ...     binder.bind(MyClass, to=CallableProvider(factory))
        ...
        >>> injector = Injector(configure)
        >>> injector.get(MyClass) is injector.get(MyClass)
        providing
        providing
        False
    """

    def __init__(self, callable: Callable[..., T]):
        self._callable = callable

    def get(self, injector: 'Injector') -> T:
        return injector.call_with_injection(self._callable)

    def __repr__(self) -> str:
        return '%s(%r)' % (type(self).__name__, self._callable)


class InstanceProvider(Provider, Generic[T]):
    """Provide a specific instance.

    ::

        >>> class MyType:
        ...     def __init__(self):
        ...         self.contents = []
        >>> def configure(binder):
        ...     binder.bind(MyType, to=InstanceProvider(MyType()))
        ...
        >>> injector = Injector(configure)
        >>> injector.get(MyType) is injector.get(MyType)
        True
        >>> injector.get(MyType).contents.append('x')
        >>> injector.get(MyType).contents
        ['x']
    """

    def __init__(self, instance: T) -> None:
        self._instance = instance

    def get(self, injector: 'Injector') -> T:
        return self._instance

    def __repr__(self) -> str:
        return '%s(%r)' % (type(self).__name__, self._instance)


@private
class ListOfProviders(Provider, Generic[T]):
    """Provide a list of instances via other Providers."""

    _providers: List[Provider[T]]

    def __init__(self) -> None:
        self._providers = []

    def append(self, provider: Provider[T]) -> None:
        self._providers.append(provider)

    def __repr__(self) -> str:
        return '%s(%r)' % (type(self).__name__, self._providers)


class MultiBindProvider(ListOfProviders[List[T]]):
    """Used by :meth:`Binder.multibind` to flatten results of providers that
    return sequences."""

    def get(self, injector: 'Injector') -> List[T]:
        return [i for provider in self._providers for i in provider.get(injector)]


class MapBindProvider(ListOfProviders[Dict[str, T]]):
    """A provider for map bindings."""

    def get(self, injector: 'Injector') -> Dict[str, T]:
        map: Dict[str, T] = {}
        for provider in self._providers:
            map.update(provider.get(injector))
        return map
