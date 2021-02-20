#!/usr/bin/python3
"""
Inherit from basemodel
"""
import models


class User(models.base_model.BaseModel):
    """class user that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
