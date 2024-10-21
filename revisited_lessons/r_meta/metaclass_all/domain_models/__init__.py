"""Domain models."""
from . import fields

from . import models

VERSION = '0.0.9'


class Photo(models.DomainModel):
    """Photo model to be attached to profile."""
    id = fields.Int()
    title = fields.String()
    path = fields.String()
    public = fields.Bool(default=False)
