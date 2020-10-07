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


# --------------------------------------------------------------------------------

nums = [97, 84, 63, 66, 29, 8, 83, 46, 58, 49, 45, 26, 13]


# basically selection_sort
# find the smallest, put it at the front, find the next smallest, put it in second place, and so forth
# best to worst case is O(n^2)

# bubble_sort
# compare first two numbers, if smaller/larger put to left or right. Look at the next three numbers
# bubbles up the largest element to the end
# best to worst case is O(n^2)



#  sorted                                               unsorted
# num = [97, 84, 63, 66, 29, 8, 83, 46, 58, 49, 45, 26, 13]
#        |    |
#         compare and then swap


# insertion_sort: --> iterative sort
# Understand
# 1) how do we know where to insert it?
# 2) how do we move the other elements over?

# Plan
def insertion_sort1(arr): #O(n^2)
# you have part of the array that is sorted
    # we can have an index ot the first element that's unsorted
    first_unsorted_index = 1
    while first_unsorted_index < len(arr): # for idx in range (1, len(arr))
        # take the next unsorted element
        # insert it into the sorted part of the array
        # swap it in place/ shift other elements to the right
        # store the element we're trying to insert into a variable
        current_element = arr[first_unsorted_index]
        # compare it to each of the elements in the sorted part of the array, going from biggest --> smallest
        sorted_index = first_unsorted_index - 1
        while  sorted_index >= 0:
            print(sorted_index)
            # if the sorted element is bigger than the current, shift the sorted element
            if arr[sorted_index] > current_element:
                arr[sorted_index + 1] = arr[sorted_index]
            # otherwise, if sorted element is < current:
            elif arr[sorted_index] < current_element:
                # we found the right place for it and we can insert it there
                arr[sorted_index + 1] = current_element
                break
            # else if you get to the end:
            if sorted_index == 0: # elif caused function to break
                arr[sorted_index] = current_element
            sorted_index = sorted_index - 1
        first_unsorted_index += 1

    return arr

print(insertion_sort1(nums))



def insertion_sort2(arr):
    # O(n^2) -> average
    # best case O(n) if list is already sorted
    # worst case backward sort
    # Keep a boundary between sort/unsorted parts of the array
    # Unsorted index points to the first unsorted element in the array
    for unsorted_index in range(1, len(arr)):
        # Current element is the first unsorted element that we're trying to insert into the sorted part of the array
        current_element = arr[unsorted_index]
        # Loop through the sorted part of th array backwards (biggest --> smallest)
        sorted_index = unsorted_index - 1
        # Stop when we reach the beginning of the array or the sorted element is <= the current element
        while sorted_index >= 0 and arr[sorted_index] > current_element:
            # If the sorted element  > current element, shift it right by 1
            arr[sorted_index + 1] = arr[sorted_index]
            # Decrement sorted index to keep looping backwards
            sorted_index -= 1
        # At this point sorted_index is the index where the current element belongs
        # Insert the current element into the array
        arr[sorted_index + 1] = current_element

    return arr