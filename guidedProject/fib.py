# 0, 1,1,2,3,5,8,13,21,34

# Recursive
# base case
# call itself
# move in the direction of the base case

# find the n-th number is nth number in the fibonacci sequence
# O(n^n)
cache = {}


def fib(n):
    if n <= 1:
        return n

    # if n in cache:
    #     return cache[n]
    # else:
    #     cache[n] = fib(n-1) + fib(n-2)
    # return cache[n]
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]


# print(fib(3))
# print(fib(5))
# print(fib(6))
# print(fib(7))
# print(fib(8))
# print(fib(9))
print(fib(50))

# memorization
# dynamic programming
# top-down dynamic programming

# O(n)


def simple_recursion(n):
    if n <= 1:
        return n
    return simple_recursion(n-1)
