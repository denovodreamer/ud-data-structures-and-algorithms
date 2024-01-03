


def sort_012(array):

    n = len(array)

    next_pos_0 = 0
    next_pos_2 = n - 1

    i = 0
    
    while i <= next_pos_2:

        value = array[i]

        if value == 0:
            array[i] = array[next_pos_0]
            array[next_pos_0] = 0

            next_pos_0 += 1
            i += 1

        elif value == 2:
            array[i] = array[next_pos_2]
            array[next_pos_2] = 2

            next_pos_2 -= 1
            
        else:
            i += 1

    return array







def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":

    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])