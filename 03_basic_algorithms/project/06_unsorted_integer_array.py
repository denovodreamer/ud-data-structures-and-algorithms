


def get_min_max(array):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = array[0]
    max = array[0]

    for integer in array:
        if integer < min:
            min = integer
        elif integer > max:
            max = integer

    return min, max


def test_random():
    ### Example Test Case of Ten Integers
    import random

    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)

    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


if __name__ == "__main__":
    test_random()



