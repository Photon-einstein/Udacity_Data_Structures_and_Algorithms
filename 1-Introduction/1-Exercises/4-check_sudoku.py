import numpy as np


# Define a function check_sudoku() here:
def check_sudoku(square):
    n = len(square)
    # check numbers <= n and integers
    if check_constrain(square, n) == False:
        return False
    # check rows
    for row in range(n):
        if check_row(square, row, n) == False:
            return False
    # check column
    for column in range(n):
        if check_column(square, column, n) == False:
            return False
    return True


def check_constrain(square, n):
    for line in range(n):
        for column in range(n):
            if (
                str(square[line][column]).isdigit() == False
                or int(square[line][column]) != square[line][column]
                or square[line][column] > n
                or square[line][column] < 1
            ):
                return False
    return True


def check_row(square, row_number, n):
    mem_check = np.zeros(n + 1)
    for i in range(n):
        mem_check[square[row_number][i]] += 1
        if mem_check[square[row_number][i]] > 1:
            return False
    return True


def check_column(square, column_number, n):
    mem_check = np.zeros(n + 1)
    for i in range(n):
        mem_check[square[i][column_number]] += 1
        if mem_check[square[i][column_number]] > 1:
            return False
    return True


# Test cases
correct = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
incorrect = [[1, 2, 3, 4], [2, 3, 1, 3], [3, 1, 2, 3], [4, 4, 4, 4]]
incorrect2 = [[1, 2, 3, 4], [2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 1, 2]]
incorrect3 = [
    [1, 2, 3, 4, 5],
    [2, 3, 1, 5, 6],
    [4, 5, 2, 1, 3],
    [3, 4, 5, 2, 1],
    [5, 6, 4, 3, 2],
]
incorrect4 = [["a", "b", "c"], ["b", "c", "a"], ["c", "a", "b"]]
incorrect5 = [[1, 1.5], [1.5, 1]]


print(check_sudoku(incorrect))
# >>> False
print(check_sudoku(correct))
# >>> True
print(check_sudoku(incorrect2))
# >>> False
print(check_sudoku(incorrect3))
# >>> False
print(check_sudoku(incorrect4))
# >>> False
print(check_sudoku(incorrect5))
# >>> False
