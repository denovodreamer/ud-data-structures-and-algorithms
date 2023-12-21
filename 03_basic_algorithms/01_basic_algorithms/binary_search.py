

##########################################################################################
# Iteration


def binary_search(array, target):
    '''Binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index)//2        # integer division in Python 3

        mid_element = array[mid_index]

        if target == mid_element:                       # we have found the element
            return mid_index

        elif target < mid_element:                      # the target is less than mid element
            end_index = mid_index - 1                   # we will only search in the left half

        else:                                           # the target is greater than mid element
            start_index = mid_element + 1               # we will search only in the right half

    return -1



##########################################################################################
# Recursive


def binary_search_recursive_soln(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
      start_index: beginning of the index of the sub-arrays
      end_index: end of the index of the sub-arrays

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index)//2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)


def binary_search_recursive(array, target):
    '''
    This function will call `binary_search_recursive_soln` function.
    You don't need to change this function.

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)

