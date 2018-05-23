#!/usr/bin/python3
import json
"""
Class Base
"""


class Base:
    """
    Class 'Base'
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        method rtrn json representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write json representation of list_objs
        """
        tmp_list = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for obj in list_objs:
                tmp_list.append(obj.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(tmp_list))

    @staticmethod
    def from_json_string(json_string):
        """
        method rtrn list of json string rep
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        method rtrns instance with pre-set values
        """
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
        elif cls.__name__ == "Square":
            tmp = cls(1)
        cls.update(tmp, **dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """
        method rtrn list of instances
        """
        tmp_list = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                tmp_list = cls.from_json_string(f.read())
            for i, j in enumerate(tmp_list):
                tmp_list[i] = cls.create(**tmp_list[i])
        except:
            pass
        return tmp_list
