from functools import wraps
from typing import Any, List


def db_execute(sql_statement, **kwargs):
    print(sql_statement)
    print(kwargs)
    return sql_statement


def redis_execute(sql_statement, **kwargs):
    print(sql_statement)
    print(kwargs)
    return sql_statement


def sql(sql_statement, processor=None):
    def sql_decorator(func):
        print(func)
        if processor is None:
            engine = db_execute
        else:
            engine = processor

        @wraps(func)
        def wrapper(*args, **kwargs):

            func_name = func.__name__
            print(f'Entering "{func_name}" function')
            sql_result = engine(sql_statement, **kwargs)
            print(sql_result)
            print(f'Result of "{func_name}" function is {sql_result}')
            print(f'Exiting from "{func_name}" function')
            return sql_result

        return wrapper

    return sql_decorator


class DatabaseRepository:
    @staticmethod
    def _sql(sql_statement):
        def sql_decorator(func):
            print(func)
            print(sql_statement)

            @wraps(func)
            def wrapper(*args, **kwargs):
                func_name = func.__name__
                print(f'Entering "{func_name}" function')
                sql_result = db_execute(sql_statement, **kwargs)
                print(sql_result)
                print(f'Result of "{func_name}" function is {sql_result}')
                print(f'Exiting from "{func_name}" function')
                return sql_result

            return wrapper

        return sql_decorator

    def __init__(self):
        pass


class AnRepository(DatabaseRepository):

    @sql(sql_statement="select * from hello where name=:name", processor=redis_execute)
    def find_kevin_redis(self, name) -> List[Any]:
        pass

    @sql(sql_statement="select * from hello where name=:name")
    def find_kevin(self, name) -> List[Any]:
        pass


result = AnRepository().find_kevin(name="test")
t = AnRepository().find_kevin_redis(name="test")
print(result)
print(t)
