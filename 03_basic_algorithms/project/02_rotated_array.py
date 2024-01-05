

def rotated_array_search(array, target):

    if target is None or len(array) == 0:
        return

    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:

        mid_index = (start_index + end_index)//2
        mid_element = array[mid_index]

        if mid_element == target:
            return mid_index

        start_element = array[start_index]
        end_element = array[end_index]

        # Left part is sorted
        if start_element < mid_element:
            if start_element <= target < mid_element:
                end_index = mid_index - 1
            else:
                start_index = mid_index + 1

        # Right part is sorted
        if end_element > mid_element:
            if mid_element < target <= end_element:
                start_index = mid_index + 1
            else:
                end_index = mid_index - 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function_1():
    arr = [6, 7, 8, 9, 10, 1, 2, 3, 4]
    target = 6
    assert rotated_array_search(arr, target) == linear_search(arr, target)


def test_function_2():
    arr = [6, 7, 8, 1, 2, 3, 4]
    target = 8
    assert rotated_array_search(arr, target) == linear_search(arr, target)


def test_function_3():
    arr = [6, 7, 8, 1, 2, 3, 4]
    target = 10
    assert rotated_array_search(arr, target) == linear_search(arr, target)


def test_null():
    arr = [1, 2, 3]
    target = None
    assert rotated_array_search(arr, target) is None


def test_empty():
    arr = []
    target = 3
    assert rotated_array_search(arr, target) is None


if __name__ == "__main__":
    test_function_1()
    test_function_2()
    test_function_3()
    test_null()
    test_empty()
