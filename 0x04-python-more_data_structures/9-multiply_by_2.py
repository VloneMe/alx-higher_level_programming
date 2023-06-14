#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    function that returns a new dictionary with all values multiplied by 2
    """
    multiplied_dic = a_dictionary.copy()
    key_list = list(multiplied_dic.keys())

    for key in key_list:
        multiplied_dic[key] *= 2

    return multiplied_dic
