def prod(a, b):
    # TODO change output to the product of a and b
    output = a * b
    return output


def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        n = output
        i = i + 1
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product


# Test cases
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120
