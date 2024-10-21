import re
from __future__ import annotations
from sqlalchemy import MetaData, select, update, delete
from sqlalchemy.orm import DeclarativeBase

DEFAULT_NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


class TableNamer:
    """
    Get Sqlalchemy table name
    """

    # pragma: no cover
    def __get__(self, obj, type):
        if type.__dict__.get('__tablename__') is None and \
            type.__dict__.get('__table__') is None:
            type.__tablename__ = re.sub(
                r'((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))', r'_\1',
                type.__name__).lower().lstrip("_")
        return getattr(type, '__tablename__', None)


class BaseEntityModel:
    """This is the base model class from where all models inherit from."""
    __metadatas__ = {}
    __tablename__ = TableNamer()
    metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    })

    def __init_subclass__(cls, **kwargs):
        bind_key = getattr(cls, '__bind_key__', None)
        if bind_key is not None:
            if bind_key not in cls.__metadatas__:
                cls.__metadatas__[bind_key] = MetaData()
            cls.metadata = cls.__metadatas__[bind_key]
        elif None not in cls.__metadatas__ and \
            getattr(cls, 'metadata', None) is not None:
            cls.__metadatas__[None] = cls.metadata
        super().__init_subclass__(**kwargs)

    @classmethod
    def select(cls):
        """Create a select statement on this model.

        Example::

            User.select().order_by(User.username)
        """
        return select(cls)

    @classmethod
    def update(cls):
        """Create an update statement on this model.

        Example::

            User.select().order_by(User.username)
        """
        return update(cls)

    @classmethod
    def delete(cls):
        """Create a delete statement on this model.

        Example::

            User.delete().where(User.username == 'susan')
        """
        return delete(cls)


class AbstractEntityModel(BaseEntityModel, DeclarativeBase):
    __abstract__ = True
