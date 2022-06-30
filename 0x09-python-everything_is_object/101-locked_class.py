#!/usr/bin/python3
"""Represents a locked class"""


class LockedClass:
    """locked class that prevents the user from
    dynamically creating new instance attributes,
    except if it is called first_name
    """
    def __init__(self, first_name=""):
        self.first_name = first_name
    __slots__ = "first_name"
