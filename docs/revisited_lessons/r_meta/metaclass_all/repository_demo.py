from typing import Union, Any

from pydantic import BaseModel
from sqlmodel import SQLModel


class RepositoryMeta(type):
    def __new__(cls, name, bases, attrs, base_type:Union[SQLModel, BaseModel, Any]=SQLModel, db_qualify='default', **kwargs):
        x = super().__new__(cls, name, bases, attrs)
        x.base_type = base_type
        x.db_qualifier = db_qualify
        return x


class HeroRepo(metaclass=RepositoryMeta):

    def find_hero(self):
        print(self)

    def find_hero_by_name_and_age(self, name, age):
        pass

    def find_hero_by_name(self, name):
        ...

    def update_name(self, name, new_name):
        pass


hero_repo = HeroRepo()
print(hero_repo)
hero_repo.find_hero()
