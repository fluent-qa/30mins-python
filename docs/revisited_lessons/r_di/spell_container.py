from typing import Optional, Set, Dict

from revisited.r_di.namespace import Namespace


class SpellContainer:
    """
    SpellContainer globally manages injection namespaces and the respective
    injectables registries.
    """
    NAMESPACES: Dict[str, Namespace] = {}

    @classmethod
    def _register_injectable(
            cls,
            klass: type,
            filepath: str,
            qualifier: str = None,
            primary: bool = False,
            namespace: str = None,
            group: str = None,
            singleton: bool = False,
    ):
        unique_id = f"{klass.__qualname__}@{filepath}"
        injectable = Injectable(klass, unique_id, primary, group, singleton)
        namespace_entry = cls._get_namespace_entry(
            namespace or cls.LOADING_DEFAULT_NAMESPACE
        )
        namespace_entry.register_injectable(injectable, klass, qualifier)
