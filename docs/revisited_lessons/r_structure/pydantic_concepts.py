# model definition
from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = 'Jane Doe'


def initialized_model():
    user = User(id='123')
    print(user)
    print(user.model_fields)
    print(user.dict())
    print(user.model_dump_json())
    print(user.model_dump())
    print(user.model_computed_fields)
    print(User.model_construct())
    print(user.model_extra)
    print(user.model_json_schema())


class Foo(BaseModel):
    count: int
    size: Optional[float] = None
    x: 'Bar' = None


class Bar(BaseModel):
    apple: str = 'x'
    banana: str = 'y'


class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]


Foo.model_rebuild()  ## update_forward_refs
Spam.model_rebuild()

def nested_model():
    spam = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
    print(spam)
    print(spam.model_fields)
    print(spam.dict())
    print(spam.model_dump_json())
    print(spam.model_dump())
    print(spam.model_computed_fields)
    print(User.model_construct())
    print(spam.model_extra)
    print(spam.model_json_schema())




if __name__ == '__main__':
    initialized_model()
    nested_model()
