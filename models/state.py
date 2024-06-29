#!/usr/bin/python3
"""State Class"""


from models.base_model import BaseModel


class State(BaseModel):
    """State Class"""
    name = ""  # Initialize name attribute

    def __init__(self, *args, **kwargs):
        """Initialize State instance"""
        super().__init__(*args, **kwargs)