#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    function that replaces or adds key/value in a dictionary
    """
    updated_dic = dict(a_dictionary)
    updated_dic[key] = value
    return updated_dic
