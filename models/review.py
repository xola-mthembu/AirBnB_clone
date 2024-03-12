#!/usr/bin/python3
"""
Review class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""   # Will be the Place.id
    user_id = ""    # Will be the User.id
    text = ""
