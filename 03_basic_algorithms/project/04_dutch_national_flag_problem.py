


def sort_012(array):

    if array is None or len(array) == 0:
        return

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



def test_function_1():
    arr = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
    assert sort_012(arr) == sorted(arr)


def test_function_2():
    arr = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
    assert sort_012(arr) == sorted(arr)


def test_function_3():
    arr = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
    assert sort_012(arr) == sorted(arr)


def test_null():
    arr = None
    assert sort_012(arr) is None


def test_empty():
    arr = []
    assert sort_012(arr) is None


if __name__ == "__main__":
    test_function_1()
    test_function_2()
    test_function_3()
    test_null()
    test_empty()
