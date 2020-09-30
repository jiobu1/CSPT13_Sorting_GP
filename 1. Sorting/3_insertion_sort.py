l = [8, 2, 5, 4, 1, 3]
tmp_var = l[1]

print("Before sorting: ", l)
# Implement an insertion sort algorithm
def insertion_sort(list_to_sort):
    # separate the first element and think of it as sorted
    # let us say it is the first item in the list

    # for all other items (on the right of the first index)
    # range based starting at index 1
    for i in range(1, len(list_to_sort)):
        # put th ecurrent number in to a temporary variable
        temp = list_to_sort[i]

        # keep track of our current index as j
        j = i

        # keep looking left, until we find where our number belongs
        # while j is greater than zero (we are not past the start of the indices)
        # and our temp variable is less than the number to the left of j
        while j > 0 and temp < list_to_sort[j-1]:
            # as we look left we can shift the items to the right as we iterate
            list_to_sort[j] = list_to_sort[j-1]
            # decrement j
            j -=1

        # when left is smaller than our temp, or we are zero, put the number at that spot
        list_to_sort[j] = temp

    # return the list back to the caller
    return list_to_sort

"""
[8, 2, 5, 4, 1, 3]
[1, 2, 3, 4, 5, 8]
"""

# lets try it
insertion_sort(l)

print("After sort: ", l)