#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel



class City(BaseModel):
    """Representation of city """
    state_id = ""
    name = ""
