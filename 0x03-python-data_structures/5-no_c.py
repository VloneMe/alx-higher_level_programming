#!/usr/bin/env python3

def no_c(my_string):
    new_str = [str for str in my_string if str != 'c' and str != 'C']
    return ("".join(new_str))
