#!/usr/bin/python3
"""
City class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""  # Will be the State.id
    name = ""
