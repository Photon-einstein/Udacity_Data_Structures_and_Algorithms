import numpy as np

def lps(input_string):     
    n = len(input_string)
    # Create a matrix of zeros
    matrix = np.zeros((n, n), dtype=int)

    # Strings of length 1 have LPS length = 1
    for i in range(n):
        matrix[i][i] = 1

    # Fill the matrix
    for s_size in range(2, n + 1):  # s_size is the size of the substring
        for start_idx in range(n - s_size + 1):
            end_idx = start_idx + s_size - 1
            if input_string[start_idx] == input_string[end_idx]:
                matrix[start_idx][end_idx] = matrix[start_idx + 1][end_idx - 1] + 2
            else:
                matrix[start_idx][end_idx] = max(matrix[start_idx][end_idx - 1], matrix[start_idx + 1][end_idx])

    # The top right cell will hold the final LPS length
    return matrix[0][n - 1]

def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = 'BxAoNxAoNxA'
solution = 5
test_case = [string, solution]
test_function(test_case)

string = 'BANANO'
solution = 3
test_case = [string, solution]
test_function(test_case)

string = "TACOCAT"
solution = 7
test_case = [string, solution]
test_function(test_case)
