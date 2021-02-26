#!/usr/bin/python3
"""
inherit from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class user that inheirts from Base model"""
    place_id = ""
    user_id = ""
    text = ""
