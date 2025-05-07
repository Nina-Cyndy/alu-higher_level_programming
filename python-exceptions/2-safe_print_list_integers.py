#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers.

    Args:
        my_list: The list containing any type of elements
        x: The number of elements to access in my_list

    Returns:
        The real number of integers printed

    Raises:
        IndexError: If x is greater than the length of my_list
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
