import sys


def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    i = 0
    assigned = False
    minimum = sys.maxsize
    for value in in_list:
        if value < minimum and value > 0:
            minimum = value
            assigned = True
    if assigned == False:
        return None
    return minimum


# Test cases
print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2
print(smallest_positive([0.2, 5, 3, -0.1, 7, 7, 6]))
# Correct output: 0.2
print(smallest_positive([-6, -9, -7]))
# Correct output: None
print(smallest_positive([]))
