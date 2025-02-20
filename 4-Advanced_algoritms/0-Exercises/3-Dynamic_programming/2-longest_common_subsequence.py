import numpy as np

def lcs(string_a, string_b):
    nRows = len(string_a) + 1
    nColumns = len(string_b) + 1
    matrix = np.zeros((nRows, nColumns))
    for row in range(1, len(string_a)+1):
        for column in range(1, len(string_b)+1):
            if string_a[row-1] == string_b[column-1]:
                matrix[row][column] = matrix[row-1][column-1] + 1
            else:
                matrix[row][column] = max(matrix[row][column-1], matrix[row-1][column]) 
    return matrix[-1][-1]

## Test cell

# Run this cell to see how your function is working
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1==5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2==7, "Incorrect LCS value."
print('Tests passed!')
