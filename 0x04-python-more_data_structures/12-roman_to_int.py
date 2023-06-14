#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    This function converts a Roman numeral to an integer.
    """
    if roman_string is None or type(roman_string) is not str:
        return 0  # Return 0 if the input is invalid

    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_chars = list(roman_string.upper())
    result = 0
    previous_value = 0

    for char in rom_chars:
        if char in values:
            result += values[char]
            if values[char] > previous_value:
                result -= previous_value * 2
            previous_value = values[char]
        else:
            return 0

    return result
