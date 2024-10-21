from datetime import datetime
from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine, Table, MetaData, DateTime
import psycopg
from sqlmodel import SQLModel, Field

pg_url = "postgresql+psycopg://postgres:changeit@127.0.0.1:5432/workspace"
apg_url = "postgresql+psycopg_async://postgres:changeit@127.0.0.1:5432/workspace"

print("create sync engine ........")
engine = create_engine(pg_url, connect_args={'options': '-c search_path=demos,public'})
print(engine)
print("create sync engine --done")

print("create async engine ........")
async_engine = create_async_engine(apg_url, echo=True)
print("create async engine --done")

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, MappedAsDataclass, DeclarativeBase, Mapped, mapped_column

Base = declarative_base()


class DemoHeroA(Base):
    __tablename__ = "demo_hero_a"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }


class DemoHero(SQLModel, table=True):
    __tablename__ = "demo_hero"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int

    def to_json(self):
        return self.model_dump()


class DemoUser(SQLModel, table=True, extend_existing=True):
    __tablename__ = "demo_user"
    __table_args__ = {'schema': 'public', 'extend_existing': True}
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    full_name: str


class BaseEntity(MappedAsDataclass, DeclarativeBase):
    pass

metadata = MetaData()

user_account_table = Table(
    "user_account",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("fullname", String),
    Column("created_at", DateTime),
)

class User(BaseEntity):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str]
    fullname: Mapped[Optional[str]]
    created_at: Mapped[datetime] = mapped_column(default_factory=datetime.utcnow)


if __name__ == '__main__':
    metadata_sqlmodel = SQLModel.metadata
    print(metadata_sqlmodel.tables)
    print(dir(metadata_sqlmodel))

    metabase_sqlalchemy = Base.metadata
    print(metabase_sqlalchemy.tables)
    print(dir(metabase_sqlalchemy))
    metabase_sqlalchemy.create_all(engine)
    metabase_sqlalchemy.create_all(engine)
    metadata.create_all(engine)

    User("spongebob", "Spongebob Squarepants")

    print(User.__table__)
