#!/usr/bin/python3

def safe_print_integer_err(value):
    """
    This function prints an integer followed by a new line.

    Args:
        value: The value to print.

    Returns:
        True if the value is correctly printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return False
    else:
        return True
