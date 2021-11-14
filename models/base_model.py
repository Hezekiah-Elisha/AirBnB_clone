#!/usr/bin/python3
"""
Class BaseModel
"""
from uuid import uuid4
from datetime import datetime
import models

# dfm = date format
dfm = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Base Model"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if hasattr(self, 'created_at') and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], dfm)
            if hasattr(self, 'updated_at') and type(self.updated_at) is str:
                self.created_at = datetime.strptime(kwargs["updated_at"], dfm)
        else:
            self.id = str(uuid4())
            self.created_at = str(datetime.now())
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """str representation"""
        s_dict = self.__dict__
        s_id = self.id
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, s_id, s_dict)

    def save(self):
        """"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        x_dict = self.__dict__.copy()
        if "created_at" in x_dict:
            x_dict["created_at"] = x_dict["created_at"].strftime(dfm)
        if "updated_at" in x_dict:
            x_dict["updated_at"] = x_dict["created_at"].strftime(dfm)
        x_dict["__class__"] = self.__class__.__name__
        return x_dict

# t = BaseModel()
# print(t)
# if __name__ == '__main__':
    # BaseModel()
