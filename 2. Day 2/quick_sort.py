# helper function / conceptual partitioning
def partition(data):
    # takes in a single list and partitions it into 3 lists -> left, pivot, right
    # create 2 empty lists (left, right)
    left = []
    right = []
    # create a pivot list containing the first element of the data
    pivot = data[0]
    # for each value in our data starting at index 1
    for value in data[1:]:
        # check if value is less than or equal to the pivot
        if value <= pivot:
            # append value to the left list
            left.append(value)
        # otherwise (the value must be greater than the pivot)
        else:
            # append value to the right list
            right.append(value)
    # returns the tuple of (left, pivot, right)
    return left, pivot, right

# quick sort that uses the partitioned data
def quicksort(data):
    # base case if th edata is an empty list return an empty list
    if data == []:
        return data

    # partition the data into 3 variables (left, pivot, right)
    left, pivot, right = partition(data)

    # recursive call to quicksort using the left
    # recursive call to quicksort using the right
    # return the concatenation of quicksort of the lhs +  pivot + rhs
    return quicksort(left) + [pivot] + quicksort(right)

# print(quicksort([5, 9, 3, 7, 2, 8, 1, 6]))

# ------------------------------------------------------------------------------
# Divide and conquer

# Quicksort
nums = [29, 84, 35, 22, 64, 97, 8, 83, 46, 58]
# [22, 8]   p = 29 [84, 35, 64, 97, 83, 46, 58]  -> smaller chunks go to the left, larger goes to right of pivot
# [8] p = 22 []    [35, 64, 97, 83, 46, 58] p = 84 [97]
# [8, 22]          [] p = 35  [64, 83, 46, 58]
# [8, 22]               [46, 58] p = 64 [83]
#                       p = 46 [58]
#    [8, 22, 29, 35, 46, 58, 64, 83, 84, 94]
# sorting version of a binary search tree


def partition1(arr):
   # choose a pivot (the first element)
    pivot = arr[0]
    # divide the array into chunks
    left = []
    right = []

    for element in arr[1:]:
        # every element < pivot goes into the "left" chunk
        if element < pivot:
            left.append(element)
        # every element > = pivot goes into the "right" chunk
        if element >= pivot:
            right.append(element)

    return left, pivot, right

def quicksort1(arr):
    # when do we stop recursing? What's our base case?
        # when there is only one element in the array
    if len(arr) <= 1: # O(1)
        return arr

    left, pivot, right = partition1(arr) # O(n)

    # quick sort the left chunks
    sorted_left = quicksort1(left) # O(n log n)
    # quick sort the right chunks
    sorted_right = quicksort1(right) # O(n log n)
    # put the chunks back together
    sort = sorted_left + [pivot] + sorted_right # O(1) or maybe O(n)

    return sort

print(quicksort1(nums))



