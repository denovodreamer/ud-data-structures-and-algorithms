

def sqrtSearch(low, high, N) :

    # If the range is still valid
    if (low <= high) :

        # Find the mid-value of the range
        mid = (low + high) // 2;

        # Base Case
        if ((mid * mid <= N) and ((mid + 1) * (mid + 1) > N)) :
            return mid;

        # Condition to check if the
        # left search space is useless
        elif (mid * mid < N) :
            return sqrtSearch(mid + 1, high, N);

        else :
            return sqrtSearch(low, mid - 1, N);

    return low;


def sqrt(target):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if target is None:
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

if __name__ == "__main__":
    test_integer_square_root()
    test_integer_square_root()
    test_null()
