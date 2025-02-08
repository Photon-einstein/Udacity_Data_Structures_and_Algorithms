"""
Problem 6: Unsorted Integer Array

In this problem, we will look for smallest and largest integer from a list of 
unsorted integers. The code should run in O(n) time. Do not use Python's 
inbuilt functions to find min and max.

You should implement the function body according to the get_min_max function 
signature. Use the test cases provided below to verify that your algorithm is 
correct. If necessary, add additional test cases to verify that your algorithm 
works correctly.
"""

from typing import Optional


def get_min_max(ints: list[int]) -> Optional[tuple[int, int]]:
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
    ints (list[int]): list of integers containing one or more integers

    Returns:
    Optional[tuple[int, int]]: A tuple containing the minimum and maximum
    integer, or None if the list is empty
    """
    if ints == None or len(ints) == 0:
        return None
    min = None
    max = None
    for i in range(len(ints)):
        if i == 0:
            min = ints[0]
            max = ints[0]
        elif min > ints[i]:
            min = ints[i]
        elif max < ints[i]:
            max = ints[i]
    return tuple[min, max]


if __name__ == "__main__":
    # Edge case: Empty input list
    res = get_min_max([])
    print(res)
    assert res == None
    print("Test 1: Empty input list pass\n")
    # Expected output: None

    # Edge case: Input list null
    res = get_min_max(None)
    print(res)
    assert res == None
    print("Test 2: Input list null pass\n")
    # Expected output: None

    # Normal case: list with negative and positive numbers
    res = get_min_max([-10, 0, 10, -20, 20])
    print(res)
    assert res == tuple[-20, 20]
    print("Test 3: List with negative and positive numbers pass\n")
    # Expected output: (-20, 20)

    # Normal case: list with large range of numbers
    res = get_min_max([1000, -1000, 500, -500, 0])
    print(res)
    assert res == tuple[-1000, 1000]
    print("Test 4: List with large range of numbers pass\n")
    # Expected output: (-1000, 1000)

    # Normal case: list with already sorted numbers
    res = get_min_max([1, 2, 3, 4, 5])
    print(res)
    assert res == tuple[1, 5]
    print("Test 5: List with already sorted numbers pass")
    # Expected output: (1, 5)
