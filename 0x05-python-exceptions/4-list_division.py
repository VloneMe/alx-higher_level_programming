def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element between two lists and returns a new list with the division results.

    Returns:
        A new list with the division results.
    """
    result_list = []

    try:
        for i in range(list_length):
            try:
                element1 = my_list_1[i] if i < len(my_list_1) else 0
                element2 = my_list_2[i] if i < len(my_list_2) else 1

                if not isinstance(element1, (int, float)) or not isinstance(element2, (int, float)):
                    raise TypeError("wrong type")

                if element2 == 0:
                    raise ZeroDivisionError("division by 0")

                result = element1 / element2
                result_list.append(result)

            except (TypeError, ZeroDivisionError) as e:
                print(str(e))

            except IndexError:
                print("out of range")

    except Exception as e:
        print(str(e))

    finally:
        return result_list[:list_length]
