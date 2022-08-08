#!/usr/bin/python3
""" definition of Base class """
import csv


class Base:
    """ Base class attributes and their definitions """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initializing class """
        Base.__nb_objects += 1
        if id is None:
            self.id = Base.__nb_objects
        else:
            self.id = id

    """ turns a list of dictionary into a string """
    @staticmethod
    def to_json_string(list_dictionaries):
        """checking for if an empty list was passed """
        if list_dictionaries is None:
            return '[]'
        elif len(list_dictionaries) == 0:
            return '[]'
        return str(list_dictionaries)

    """ class method to write json string into a file """
    @classmethod
    def save_to_file(cls, list_objs):
        """ creating new list to hold the json strings"""
        new_dict = {}
        file_name = ""
        new_list = []
        new_str = ""

        if list_objs is not None:
            for obj in list_objs:
                new_dict = obj.to_dictionary()
                new_list.append((new_dict))
                new_str = Base.to_json_string(new_list)
        else:
            new_str = '[]'
        file_name = (cls.__name__)
        file_name += ".json"
        with open(file_name, 'w') as f:
            f.write(new_str)

    """ method to turn a json string into a list """
    @staticmethod
    def from_json_string(json_string):
        """checking if 'json_string is None or empty """
        new_list = []

        if json_string is None:
            return new_list
        elif len(json_string) == 0:
            return new_list
        new_list = eval(json_string)
        return new_list

    """ changes a dictionary to instant """
    @classmethod
    def create(cls, **dictionary):
        """ checking for what class as passed as argument """
        if cls.__name__ == "Square":
            s = cls(2)
            s.update(**dictionary)
            return s
        else:
            r = cls(5, 3)
            r.update(**dictionary)
            return r

    """ method creates an instance using information from a json file"""
    @classmethod
    def load_from_file(cls):
        """ setting file name """
        filename = cls.__name__
        filename += '.' + "json"
        new_list = []
        new_list2 = []
        new_str = ""

        try:
            with open(filename, 'r') as f:
                new_str = f.read()
                new_list2 = cls.from_json_string(new_str)
                for diction in new_list2:
                    new_list.append(cls.create(**diction))
                return new_list
        except FileNotFoundError:
            return []
    """ method saves data to a csv file """
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ opening file in write mode """
        filename = cls.__name__
        main_list = []
        i = 0

        filename += '.' + 'csv'
        with open(filename, 'w') as f:
            write = csv.writer(f)
            for obj in list_objs:
                my_dict = obj.to_dictionary()
                new_list = list(my_dict.keys())
                if i == 0:
                    main_list.append(new_list)
                new_list = list(my_dict.values())
                main_list.append(new_list)
                i += 1
            write.writerows(main_list)

    """ method reads data from csv file then creates a list of instances
    from it"""
    @classmethod
    def load_from_file_csv(cls):
        """ opening file in read mode """
        my_list = []
        i = 0
        new_list = []
        new_dict = {}
        obj_list = []
        filename = cls.__name__
        filename += '.' + 'csv'

        with open(filename, 'r') as f:
            my_list = list(csv.DictReader(f))
            for dictionary in my_list:
                for k, v in dictionary.items():
                    new_dict[k] = int(v)
                obj_list.append(cls.create(**new_dict))
        return obj_list
