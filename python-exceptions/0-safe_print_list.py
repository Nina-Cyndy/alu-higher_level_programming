#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.
    
    Args:
        my_list: The list to print elements from (can contain any type)
        x: The number of elements to print
        
    Returns:
        The real number of elements printed
    """
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        # This happens when x is bigger than the length of my_list
        pass
    finally:
        print("")
    return count
