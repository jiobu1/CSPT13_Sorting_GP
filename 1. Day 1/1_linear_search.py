# Linear Search

"""
Key Points
- Linear search is the simplest type of search we can do
- Sometimes it's the only method available. If the data is unordered, this is the only way to do it
- It also beats a binary search under some special circumstances
- Key words: unsorted, random
"""

import random
import time  # We'll use this later

my_range = 100
my_size = 100

my_random = random.sample(range(my_range), my_size)
print(my_random)

searching_for = 7

# O(n)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True

    return False

# another function
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i

#     return -1

# Binary Search

"""
Key Points
- Binary search requires sorted data
- Each pass, we cut the remaining possibilities by half, hence the term binary
- Key words: sorted, ordered
"""

def find_value_binary(arr, value):
    first = 0

    last = (len(arr) - 1)

    found = False

    while first <= last and not found:
        # find the middle of the data
        middle = (first + last) // 2

        if arr[middle] == value:
            found = True

        else:
            # left case
            if value < arr[middle]:
                last = middle - 1
            else:
                # right case
                # search the upper half
                first = middle + 1

    return found


# Comparing Linear vs. Binary

"""
Key Points
- Binary search is only faster if the data is already sorted.
- It's slower for the first search if the data needs to be sorted first
- Subsequent searches will be much faster
"""

# print("Linear")
# start = time.time()
# print(linear_search(my_random, searching_for))
# end = time.time()
# print(f"Runtime: {end - start}")

# print("Binary")
# start = time.time()
# my_random.sort()
# print(find_value_binary(my_random, searching_for))
# end = time.time()
# print(f"Runtime: {end - start}")


# # lets see what heppens with multiple runs

# print("Linear")
# start = time.time()
# print(linear_search(my_random, searching_for))
# end = time.time()
# print(f"Runtime: {end - start}")

# print("Linear Again")
# start = time.time()
# print(linear_search(my_random, searching_for))
# end = time.time()
# print(f"Runtime: {end - start}")

# print("Binary")
# start = time.time()
# my_random.sort()
# print(find_value_binary(my_random, searching_for))
# end = time.time()
# print(f"Runtime: {end - start}")

# print("Binary _after_ sort")
# start = time.time()
# print(find_value_binary(my_random, searching_for))
# end = time.time()
# print(f"Runtime: {end - start}")

random_range = 100000000
size = 1500000

nums = [28, 97, 84, 63, 66, 29, 98, 68, 96, 89, 15, 67, 8 ,83, 46, 58, 49, 45, 26, 13]
# unsorted, has to go through each number 1 by

my_target = 45

sorted_nums = sorted(nums)

def linear_search1(arr, target): # 0(n)
    """
    Returns true if it target is in arr, else false
    """
    # Loop through the array
    for i in arr:
        #compare values
        if i == target:
            return True
        # Finish looping:
        # We didn't find it, return False
    return False

sort = [8, 13, 15, 26, 28, 29, 45, 46, 49, 58, 63, 66, 67, 68, 83, 84, 89, 96, 97, 98]
# Sorts -> splits in half, if it is lower than the middle it throws away the numbers after the middle
# if the number is greater, it throws away the lower numbers
# O(log n)

def binary_search(arr, target):
    """
    Returns true if target is in arr, else false
    """
    # Remember to check the empty case

    # start and end index in variables
    # pass around slices of the array - creates a new array, would use extra memory and time, you also lose the original indices.
    # Start = the starting index of the subset of the array we're searching in. Inclusive
    # End = the end index of the subset --> inclusive
    start = 0
    end = len(arr)-1

    # High level algorithm:
    # How do we know if it's not found?
    # the subset that we're looking at has 0 or negative length
    while end >= start:
        # Look at the middle
        # how do we get the midpoint?

            # for the whole array, it's len(arr)/ 2-1
            # for a subset of the array: (start + end)//2

            middle_index = (start + end)//2
            middle_value = arr[middle_index]

            # Compare it to the target
            # How to represent the subset/ "window" that we're searching in?
            # start index + length of the subarray
            if target == middle_value:
                return True
            if target > middle_value:
                # search the right side -> set start = middle_index + 1
                start = middle_index + 1
            if target < middle_value:
                # search the left side - > set end = middle_index -1
                end = middle_index - 1
            # Repeat

    # if not found, return False
    return False

# print(nums, my_target)
# print(linear_search1(nums, my_target))

# print(sorted_nums, my_target)
# print(linear_search1(sorted_nums, my_target))

# print(sorted_nums, my_target)
# print(binary_search(sorted_nums, 96)) -> works

start = time.time()
linear_search1(nums, my_target)
end = time.time()
print(f"Linear search array of length {len(nums)} took {end-start} seconds")

sorted_nums = sorted(nums)

start = time.time()
binary_search(sorted_nums, my_target)
end = time.time()
print(f"Binary search array of length {len(sorted_nums)} took {end-start} seconds")


