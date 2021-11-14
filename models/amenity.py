#!/usr/bin/python3
"""Class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents a City"""
    name = ''

    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
