"""
Problem 2: Search in a Rotated Sorted Array

You are given a sorted array that has been rotated at a random pivot point. 
For example, [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].

You are also given a target value to search for. If the target is found in the 
array, return its index; otherwise, return -1. Assume there are no duplicates 
in the array, and the runtime complexity of your algorithm must be O(log n).

You should implement the function body according to the rotated_array_search 
function signature. Use the test cases provided below to verify that your 
algorithm is correct. If necessary, add additional test cases to verify that 
your algorithm works correctly.
"""


def rotated_array_search(input_list: list[int], number: int) -> int:
    """
    Find the index by searching in a rotated sorted array

    Args:
    input_list (list[int]): Input array to search
    number (int): Target number to find

    Returns:
    int: Index of the target number or -1 if not found
    """
    if input_list == None or len(input_list) == 0:
        return -1
    return binarySearch(input_list, 0, len(input_list) - 1, number)


def binarySearch(arr: list[int], low: int, high: int, number: int) -> int:
    """
    Finds the index of number is it exists in the arr list, otherwise
    it will return -1.

    Args:
    input_list (list[int]): Input array to search
    low (int): lower bound of the index to perform the binary search
    high (int): upper bound of the index to perform the binary search, inclusive
    number (int): Target number to find

    Returns:
    int: Index of the target number or -1 if not found
    """
    if high >= low:
        mid = low + (high - low) // 2

        if arr[mid] == number:
            return mid
        elif arr[low] < arr[high]:
            if arr[mid] < number:
                return binarySearch(arr, mid + 1, high, number)
            else:
                return binarySearch(arr, low, mid - 1, number)
        else:
            left_search = binarySearch(arr, low, mid - 1, number)
            if left_search != -1:
                return left_search
            return binarySearch(arr, mid + 1, high, number)
    else:
        return -1


# Test function using provided test cases
def test_function(test_case: list[list[int], int]) -> None:
    """
    Test the rotated_array_search function with a given test case.

    Args:
    test_case (list[list[int], int]): A list containing two elements:
        - A list of integers representing the input array to search.
        - An integer representing the target number to find.

    Returns:
    None: Prints "Pass" if the rotated_array_search function returns the same
    result as the linear_search function, otherwise prints "Fail".
    """
    input_list: list[int] = test_case[0]
    number: int = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


def linear_search(input_list: list[int], number: int) -> int:
    """
    Perform a linear search for a target number in a list of integers.

    Args:
    input_list (list[int]): The list of integers to search through.
    number (int): The target number to find in the list.

    Returns:
    int: The index of the target number if found, otherwise -1.
    """
    if input_list == None:
        return -1
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


if __name__ == "__main__":
    # Edge case: Empty input list
    test_function([[], 5])
    # Expected output: Pass

    # Edge case: Input list null
    test_function([None, 10])
    # Expected output: Pass

    # Normal case: Number at the beginning of the list
    test_function([[4, 5, 6, 7, 0, 1, 2], 4])
    # Expected output: Pass

    # Normal case: Number at the end of the list
    test_function([[4, 5, 6, 7, 0, 1, 2], 2])
    # Expected output: Pass

    # Normal case: Number in the middle of the list
    test_function([[4, 5, 6, 7, 0, 1, 2], 6])
    # Expected output: Pass
