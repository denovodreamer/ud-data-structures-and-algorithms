


def get_min_max(array):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if array is None:
        return

    if len(array) == 0:
        return []

    min = array[0]
    max = array[0]

    for integer in array:
        if integer < min:
            min = integer
        elif integer > max:
            max = integer

    return min, max


def test_null():
    array = None
    assert get_min_max(array) is None


def test_empty():
    array = []
    assert len(get_min_max(array)) == 0


def test_random():
    ### Example Test Case of Ten Integers
    import random

    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)

    assert (0, 9) == get_min_max(l)


if __name__ == "__main__":
    test_null()
    test_empty()
    test_random()



