#!/usr/bin/python3
"""
inherit from BaseModel
"""

class Place(models.base_model.BaseModel):
    """class user that inheirts from Base model"""
     city_id = ""
     user_id = ""
     description=""
     number_rooms=""
     max_guest= 0
     price_by_night = 0
     latitude = 0.0
     longitude = 0.0
     amenity_ids =""
     name = ""
