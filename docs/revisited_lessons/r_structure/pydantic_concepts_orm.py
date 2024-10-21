from __future__ import annotations

import typing
from typing import List

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import declarative_base
from sqlmodel import Field
from typing_extensions import Annotated
import sqlalchemy as sa

from pydantic import BaseModel, ConfigDict, StringConstraints

Base = declarative_base()


class CompanyOrm(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)
    domains = Column(ARRAY(String(255)))


class CompanyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    public_key: Annotated[str, StringConstraints(max_length=20)]
    name: Annotated[str, StringConstraints(max_length=63)]
    domains: List[Annotated[str, StringConstraints(max_length=255)]]


co_orm = CompanyOrm(
    id=123,
    public_key='foobar',
    name='Testing',
    domains=['example.com', 'foobar.com'],
)
print(co_orm)
# > <__main__.CompanyOrm object at 0x0123456789ab>
co_model = CompanyModel.model_validate(co_orm)
print(co_model)
"""
id=123 public_key='foobar' name='Testing' domains=['example.com', 'foobar.com']
"""
import typing

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

from pydantic import BaseModel, ConfigDict, Field


class MyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    metadata: typing.Dict[str, str] = Field(alias='metadata_')


Base = declarative_base()


class SQLModel(Base):
    __tablename__ = 'my_table'
    id = sa.Column('id', sa.Integer, primary_key=True)
    # 'metadata' is reserved by SQLAlchemy, hence the '_'
    metadata_ = sa.Column('metadata', sa.JSON)


sql_model = SQLModel(metadata_={'key': 'val'}, id=1)

pydantic_model = MyModel.model_validate(sql_model)

print(pydantic_model.model_dump())
# > {'metadata': {'key': 'val'}}
print(pydantic_model.model_dump(by_alias=True))
# > {'metadata_': {'key': 'val'}}
