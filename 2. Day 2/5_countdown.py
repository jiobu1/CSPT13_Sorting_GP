"""
One of the most straightforward problems we can solve recursively is to print every number from n down to zero
in succession. We can do that simply by writing a function that prints n, then calls itself for n-1:

What is a recursive function? -> a function calls itself, has a stopping point (base case)

"""
# import sys
import sys
# sys.setrecursionlimit(10005)
# N = 10000 # too large

# n = 100

# def countdown_i(n):
#     # while loop version
#     while (n > 0): # condition and label
#         print(n) # body
#         n -= 1 # decrement

# def countdown(n): # label
#     # condition (base case)
#     if n == 0:
#         return

#     # body
#     print(n)

#     # decrement
#     countdown(n-1)

# # countdown_i(n)
# # countdown(N)
# countdown(n)

def countdown1(n):
    """ Prints outs all numbers from n to zero (inclusive) """
    for i in range(n, -1, -1):
        print(i)

# countdown1(4)

def recursive_countdown(n):
    """ Prints outs all numbers from n to zero (inclusive) """
    # Recursive versions:
    # print out n
    # call countdown to print out n-1 through zero
    # have to keep track of the call stack
    print(n)

    if n == 0:
        return

    recursive_countdown(n-1)

# recursive_countdown(4)

def double_countdown(n): # O(2^n) -> exponential
    print(n)

    if n == 0:
        return

    double_countdown(n-1)
    double_countdown(n-1)

double_countdown(3)

# 32103210
#33221100

#Actual
# 321001002100100

# o(2^n) aka exponential
# n = 1 -- ~ 3
# n = 2 -- ~ 7
# n = 3 -- ~ 15
# n = 4 -- ~ 31
# n = 5 -- ~ 63

