#!/usr/bin/python3


def safe_function(fct, *args):
    """
    This executes a function safely with the given arguments.

    Args:
        fct: The function to execute.
        *args: Variable number of arguments to pass to the function.

    Returns:
        The result of the function.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return None
