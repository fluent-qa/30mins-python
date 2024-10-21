from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, PositiveInt, ValidationError


class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',
    'tastes': {
        'wine': 9,
        b'cheese': 7,
        'cabbage': '1',
    },
}


def model_usage_example():
    user = User(**external_data)

    print(user.id)
    # > 123
    print(user.model_dump())
    """
    {
        'id': 123,
        'name': 'John Doe',
        'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
        'tastes': {'wine': 9, 'cheese': 7, 'cabbage': 1},
    }
    """


def model_validation_example():
    external_data = {'id': 'not an int', 'tastes': {}}
    try:
        user = User(**external_data)
        print(user.id)
    except ValidationError as e:
        print(e)
        print(e.errors())


if __name__ == '__main__':
    model_usage_example()
    model_validation_example()
