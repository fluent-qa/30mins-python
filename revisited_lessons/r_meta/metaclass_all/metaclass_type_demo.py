from pydantic import BaseModel
from sqlmodel import SQLModel


class MyMeta(type):
    def __new__(cls, name, bases, class_dict, arg1, arg2, **kwargs):
        # Access the arguments passed from the class
        print(f"Metaclass received arguments: arg1={arg1}, arg2={arg2} change={kwargs['change']}")

        # Call the parent metaclass's __new__ method
        return super().__new__(cls, name, bases, class_dict)


class MyClass(metaclass=MyMeta, arg1="value1", arg2="value2", change="test"):
    # Class definition goes here
    pass


print(MyClass())
print(MyClass.__dict__)


class ModelEntity(BaseModel):
    name: str


class RepositoryMeta(type):
    def __new__(cls, name, bases, attrs, base_type=SQLModel, db_qualify='default', **kwargs):
        x = super().__new__(cls, name, bases, kwargs)
        x.base_type = base_type
        x.db_qualifier = db_qualify
        return x


class BaseRepository:

    def __init__(self):
        print("BaseRepository initialized")

    def find_it(self):
        print("test_item")
        print(self)


class ToDoRepo(BaseRepository, metaclass=RepositoryMeta, base_type=ModelEntity, db_qualifier="new"):

    @staticmethod
    def child_method():
        print("child_method", ToDoRepo.base_type)


todo = ToDoRepo()
print(todo.base_type, todo.db_qualifier)
todo.find_it()
todo.child_method()
# print(getattr(BaseRepository, 'base_type'))
# print(getattr(BaseRepository, 'db_qualifier'))
