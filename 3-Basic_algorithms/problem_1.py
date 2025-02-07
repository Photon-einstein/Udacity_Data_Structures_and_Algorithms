"""
Problem 1: Square Root of an Integer

In this problem, you need to find the square root of a given integer without using 
any Python libraries. You should return the floor value of the square root.

Below is a function signature that serves as a starting point for your implementation. 
Your task is to complete the body of the function. Additionally, some test cases are 
provided to help you verify the correctness of your implementation. If necessary, add 
test cases to verify that your algorithm is working properly.

The expected time complexity is O(log(n)).
"""


def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
    number(int): Number to find the floored square root

    Returns:
    int: Floored square root
    """
    if number == 0 or number == 1:
        return number
    return binarySearch(number, 1, number // 2)


def binarySearch(number: int, low: int, high: int) -> int:
    """
    Finds the floored square root of the integer number

    Args:
    number(int): Number to find the floored square root
    low (int): lower bound of the value of the floored square root
    high (int): upper bound of the value of the floored square root

    Returns:
    int: Floored square root
    """
    if high >= low:
        mid = low + (high - low) // 2

        floor_root_squared = mid * mid
        upper_root_squared = (mid + 1) * (mid + 1)

        if floor_root_squared == number or (
            floor_root_squared < number and upper_root_squared > number
        ):
            return mid
        elif floor_root_squared < number:
            return binarySearch(number, mid + 1, high)
        else:
            return binarySearch(number, low, mid - 1)
    else:
        return 0


if __name__ == "__main__":
    # Test cases
    print("Pass" if 3 == sqrt(9) else "Fail")  # Expected Output: Pass
    print("Pass" if 0 == sqrt(0) else "Fail")  # Expected Output: Pass
    print("Pass" if 4 == sqrt(16) else "Fail")  # Expected Output: Pass
    print("Pass" if 1 == sqrt(1) else "Fail")  # Expected Output: Pass
    print("Pass" if 5 == sqrt(27) else "Fail")  # Expected Output: Pass
    print("Pass" if 11 == sqrt(125) else "Fail")  # Expected Output: Pass
    print("Pass" if 76 == sqrt(5786) else "Fail")  # Expected Output: Pass
