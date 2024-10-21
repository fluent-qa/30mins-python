## https://docs.pydantic.dev/2.0/usage/validators/
from pydantic import BaseModel, validator, field_validator

from typing import List

from typing_extensions import Annotated

from pydantic import BaseModel, ValidationError, field_validator
from pydantic.functional_validators import AfterValidator


def check_squares(v: int) -> int:
    assert v ** 0.5 % 1 == 0, f'{v} is not a square number'
    return v


def check_cubes(v: int) -> int:
    # 64 ** (1 / 3) == 3.9999999999999996 (!)
    # this is not a good way of checking cubes
    assert v ** (1 / 3) % 1 == 0, f'{v} is not a cubed number'
    return v


SquaredNumber = Annotated[int, AfterValidator(check_squares)]
CubedNumberNumber = Annotated[int, AfterValidator(check_cubes)]
# MyVal = Annotated[int, AfterValidator(func1), BeforeValidator(func2)]


class User(BaseModel):
    id: int
    name: str
    age: int
    email: str
    square_numbers: List[SquaredNumber] = []
    cube_numbers: List[CubedNumberNumber] = []

    @field_validator('square_numbers', 'cube_numbers', mode='before')
    def split_str(cls, v):
        if isinstance(v, str):
            return v.split('|')
        return v

    @field_validator('cube_numbers', 'square_numbers')
    def check_sum(cls, v):
        if sum(v) > 42:
            raise ValueError('sum of numbers greater than 42')
        return v

    @field_validator('age')
    def age_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('年龄必须大于0')
        return value

    @field_validator('email')
    def email_must_be_valid(cls, value):
        if "@" not in value:
            raise ValueError('请输入有效的电子邮件地址')
        return value

    @field_validator('name')
    def name_cannot_be_empty(cls, values):
        if not values:
            raise ValueError('姓名不能为空')
        return values


user_data = {
    "id": 1,
    "name": "",
    "age": -10,
    "email": "invalid_email"
}

try:
    user = User(**user_data)
except ValueError as e:
    print(f"验证失败: {e}")
else:
    print(f"验证成功: {user}")


## TODO: field validator, model validator
