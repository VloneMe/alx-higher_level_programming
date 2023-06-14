#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    function that returns a set of common elements in two sets
    """
    comm_set = (set_1 & set_2)
    return comm_set
