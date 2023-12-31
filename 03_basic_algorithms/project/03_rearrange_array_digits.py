
def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def mergesort(items):

    if len(items) <= 1:
        return items

    # Divide
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    # Conquer
    left = mergesort(left)
    right = mergesort(right)

    # Combine
    merge_sort = merge(left, right)

    return merge_sort


def rearrange_digits(arr):

    arr_sorted = mergesort(arr)

    number_1 = 0
    number_2 = 0

    for i in range(len(arr_sorted)):
        if i%2 == 0:
            number_1 = 10 * number_1 + arr_sorted[i]
        else:
            number_2 = 10 * number_2 + arr_sorted[i]

    return [number_1, number_2]


def test_1():
    arr = [1, 2, 3, 4, 5]
    assert rearrange_digits(arr) == [531, 42]


def test_2():
    arr = [4, 6, 2, 5, 9, 8]
    assert rearrange_digits(arr) == [964, 852]


if __name__ == "__main__":
    test_1()
    test_2()