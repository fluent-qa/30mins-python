from typing import Annotated, Dict, List, Literal, Tuple

from annotated_types import Gt

from pydantic import BaseModel, field_validator


# Type hint powering schema validation
class Fruit(BaseModel):
    name: str
    color: Literal['red', 'green']
    weight: Annotated[float, Gt(0)]
    bazam: Dict[str, List[Tuple[int, bool, float]]]


print(
    Fruit(
        name='Apple',
        color='red',
        weight=4.2,
        bazam={'foobar': [(1, True, 0.1)]},
    )
)
# > name='Apple' color='red' weight=4.2 bazam={'foobar': [(1, True, 0.1)]}
## performance: pydantic-core: implemented by rust
## function validators

## serialization

from datetime import datetime, timezone

from pydantic import BaseModel


class Meeting(BaseModel):
    when: datetime
    where: bytes
    why: str = 'No idea'


m = Meeting(when='2020-01-01T12:00', where='home')
print(m.model_dump(exclude_unset=True))  # to dict
# > {'when': datetime.datetime(2020, 1, 1, 12, 0), 'where': b'home'}
print(m.model_dump(exclude={'where'}, mode='json'))  # to dict
# > {'when': '2020-01-01T12:00:00', 'why': 'No idea'}
print(m.model_dump_json(exclude_defaults=True))  # to json
# > {"when":"2020-01-01T12:00:00","where":"home"}

# to json schema
print(Meeting.model_json_schema())

m = Meeting.model_validate({'when': '2020-01-01T12:00', 'where': 'home'})
print(m)
m = Meeting.model_validate({'when': '2020-01-01T12:00', 'where': 'home'}, strict=True)
print(m)

# - BaseModel
# - dataclasses
# - TypeAdapter
# - validate_call

from datetime import datetime

from typing_extensions import NotRequired, TypedDict

from pydantic import TypeAdapter


class Meeting(TypedDict):
    when: datetime
    where: bytes
    why: NotRequired[str]

    @field_validator('when', mode='wrap')
    def when_now(cls, input_value, handler):
        if input_value == 'now':
            return datetime.now()
        when = handler(input_value)
        # in this specific application we know tz naive datetimes are in UTC
        if when.tzinfo is None:
            when = when.replace(tzinfo=timezone.utc)
        return when


meeting_adapter = TypeAdapter(Meeting)
m = meeting_adapter.validate_python(
    {'when': '2020-01-01T12:00', 'where': 'home'}
)
print(m)
# > {'when': datetime.datetime(2020, 1, 1, 12, 0), 'where': b'home'}
meeting_adapter.dump_python(m, exclude={'where'})

print(meeting_adapter.json_schema())
"""
{
    'properties': {
        'when': {'format': 'date-time', 'title': 'When', 'type': 'string'},
        'where': {'format': 'binary', 'title': 'Where', 'type': 'string'},
        'why': {'title': 'Why', 'type': 'string'},
    },
    'required': ['when', 'where'],
    'title': 'Meeting',
    'type': 'object',
}
"""
print(Meeting(when='2020-01-01T12:00+01:00'))
# > when=datetime.datetime(2020, 1, 1, 12, 0, tzinfo=TzInfo(+01:00))
print(Meeting(when='now'))
# > when=datetime.datetime(2032, 1, 2, 3, 4, 5, 6)
print(Meeting(when='2020-01-01T12:00'))
# > when=datetime.datetime(2020, 1, 1, 12, 0, tzinfo=datetime.timezone.utc)
