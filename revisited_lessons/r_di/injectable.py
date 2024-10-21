from typing import Optional, Callable, Any, Set, Dict

from pydantic import BaseModel


class Injectable(BaseModel):
    name: str = None
    arg_spec: Any = None
    type_name: Optional[str] = None
    handler: Callable = None
    handler_cls: Callable = None
    handler_cls_constructor: Callable = None
    group: Optional[str] = None
    singleton: bool = False
    scope: str = None
