"""
Problem 3: Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is 
maximum. Return these two numbers. You can assume that all array elements are 
in the range [0, 9]. The number of digits in both the numbers cannot differ by 
more than 1. You're not allowed to use any sorting function that Python 
provides and the expected time complexity is O(nlog(n)).

You should implement the function body according to the rearrange_digits 
function signature. Use the test cases provided below to verify that your 
algorithm is correct. If necessary, add additional test cases to verify that 
your algorithm works correctly.

For example, if [1, 2, 3, 4, 5] is given, the expected answer would be [531, 42]. 
Another expected answer can be [542, 31]. 
In scenarios such as these when there are more than one possible answers, return any one.
"""


def rearrange_digits(input_list: list[int]) -> tuple[int, int]:
    """
    Rearrange the digits of the input list to form two numbers such that their
    sum is maximized.

    This function sorts the input list in descending order and then alternates
    the digits to form two numbers.

    Args:
    input_list (list[int]): A list of integers to be rearranged.

    Returns:
    tuple[int, int]: A tuple containing two integers formed by rearranging the
    digits of the input list.
    """
    if len(input_list) == 0:
        return (0, 0)

    sorted_list = merge_sort(input_list)  # O(n log n)

    start_index_first_tuple_element = 0
    start_index_second_tuple_element = 1
    step = 2

    return (  # O(n)
        calculate_tuple_element_value(
            sorted_list, start_index_first_tuple_element, step
        ),
        calculate_tuple_element_value(
            sorted_list, start_index_second_tuple_element, step
        ),
    )


def calculate_tuple_element_value(list: list[int], start: int, step: int) -> int:
    n = 0
    for i in range(start, len(list), step):
        n = n * 10 + list[i]
    return n


def merge_sort(arr):
    """Performs merge sort on the input array."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """Merges two sorted lists in descending order."""
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:  # Sort in descending order
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


def test_function(test_case: tuple[list[int], list[int]]) -> None:
    """
    Test the rearrange_digits function with a given test case.

    Args:
    test_case (tuple[list[int], list[int]]): A tuple containing two elements:
        - A list of integers representing the input array to be rearranged.
        - A list of two integers representing the expected output.

    Returns:
    None: Prints "Pass" if the sum of the output from rearrange_digits matches
    the sum of the expected output, otherwise prints "Fail".
    """
    output: tuple[int, int] = rearrange_digits(test_case[0])
    solution: list[int] = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    # Edge case: Single element list
    test_function(([9], [9, 0]))
    # Expected output: Pass

    # Normal case: Mixed positive and negative numbers
    test_function(([1, 2, 3, 4, 5], [542, 31]))
    # Expected output: Pass

    # Normal case: list with zeros
    test_function(([0, 0, 0, 0, 0], [0, 0]))
    # Expected output: Pass

    # Normal case: list with repeated numbers
    test_function(([2, 2, 2, 2, 2], [222, 22]))
    # Expected output: Pass

    # Edge case: list with no numbers
    test_function(([], []))
    # Expected output: Pass
