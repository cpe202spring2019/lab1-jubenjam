
def max_list_iter(int_list):  # must use iteration not recursion
    if type(int_list) != list:
        raise ValueError
    if len(int_list) == 0:
        return None
    max = 0
    for i in int_list:
        if i > max:
           max = i
    return max
        
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""


def reverse_rec(int_list):   # must use recursion
    if type(int_list) != list:
        raise ValueError
    if len(int_list) == 0:
        return []
    if len(int_list) == 1:
        return int_list
    first = int_list[0]
    int_list.remove(first)
    x = reverse_rec(int_list)
    x.append(first)
    return x
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""

def bin_search(target, low, high, int_list):  # must use recursion
    if type(int_list) != list:
        raise ValueError
    if high < low:
       return None
    if int_list[high] == target:
       return high
    return bin_search(target, low, high - 1, int_list)
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
