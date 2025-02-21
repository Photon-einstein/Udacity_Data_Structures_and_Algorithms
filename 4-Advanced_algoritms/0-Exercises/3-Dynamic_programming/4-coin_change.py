def coin_change(coins, amount):

    # TODO: Complete the coin_change function
    # This should return one value: the fewest coins needed to make up the given amount
    # Base cases
    if amount < 0:  return float('inf')
    if amount == 0: return 0 
    
    coins.sort()
    amountSum = 0
    solution = 0
    while amountSum != amount:
        found = False
        for i in range(len(coins)-1, -1, -1):
            if amountSum + coins[i] <= amount:
                amountSum +=coins[i]
                solution +=1
                found = True
                break;
        if found == False:
            return -1
    return solution

def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [1,2,5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)

arr = [1,4,5,6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
test_function(test_case)

arr = [5,7,8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)