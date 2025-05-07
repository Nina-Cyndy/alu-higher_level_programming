#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists.

    Args:
        my_list_1: First list (can contain any type)
        my_list_2: Second list (can contain any type)
        list_length: Length of the new list

    Returns:
        New list with all divisions (length = list_length)
    """
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result = 0
            else:
                result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            new_list.append(result)
    return new_list
