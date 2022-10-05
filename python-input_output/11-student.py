#!/usr/bin/python3
"""

A module that representes a class Student

"""


class Student:
    """
    A class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            my_dict = {}
            for i in attrs:
                for k, v in self.__dict__.items():
                    if i == k:
                        my_dict.update({k: v})
            return my_dict

    def reload_from_json(self, json):
        for k, v in self.__dict__.items():
            self.__dict__[k] = json[k]
