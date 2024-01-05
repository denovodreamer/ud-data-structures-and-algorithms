

def sqrt(target):
    """
    Computes the floored square root of a number.
    """

    if target is None or target < 0:
        return

    # Then initial range goes from 1 to the target
    start = 1
    end = target
    middle = (start + end)//2

    while start < middle:

        # Square value of the middle element
        middle_squared = middle**2

        if target == middle_squared: # Squared root was found
            return middle
        elif target < middle_squared:  # Move to the left part of the range
            end = middle
        else:   # Move to the right part of the range
            start = middle

        middle = (start + end)//2

    return middle


def test_integer_square_root():
    """
    Tests the case when the squared root is an integer value.
    """
    target = 25
    assert sqrt(target) == 5


def test_integer_square_root():
    """
    Tests the case when the squared root is a float value
    and if the resulting value is the floor of the true value.
    """
    import math
    target = 27
    assert sqrt(target) == math.floor(math.sqrt(target))


def test_null():
    """
    Tests the edge case when the input is null.
    """
    target = None
    assert sqrt(target) is None

def test_negative():
    """
    Tests the edge case when the input is negative.
    """
    target = -5
    assert sqrt(target) is None

if __name__ == "__main__":
    test_integer_square_root()
    test_integer_square_root()
    test_null()
    test_negative()
