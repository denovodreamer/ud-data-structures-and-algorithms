



def rotated_array_search(array, target):
    
    start_index = 0
    end_index = len(array) - 1

    i = 0
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


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
    test_function([[], 10])


  
    print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 7))