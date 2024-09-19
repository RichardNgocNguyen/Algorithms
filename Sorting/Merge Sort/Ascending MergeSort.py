import random
import time


def mergesort(array, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if left < right:
        # Finds the midpoint in the array
        mid = (left + right) // 2
        # Calls the mergesort function recursively to create the first half
        mergesort(array, left, mid)
        # Calls the mergesort function recursively to create the second half
        mergesort(array, mid + 1, right)
        # Calls this function to perform not in-place sorting to combine the first and second half of array
        merge(array, left, mid, right)


def merge(array, left, mid, right):
    # Length of the first array
    n1 = mid - left + 1
    # Length of second array
    n2 = right - mid

    left_arr = []
    right_arr = []
    # Creates the first array starting at position left to left + n1
    for i in range(left, left + n1):
        left_arr.append(array[i])
    # Creates the second array from position left + n1 to (left + n1) + n2
    for j in range(left + n1, left + n1 + n2):
        right_arr.append(array[j])
    # Appends an infinitely positive number to both arrays that acts as a stopper
    left_arr.append(9999999999)
    right_arr.append(9999999999)
    i = 0
    j = 0
    for k in range(left, right + 1):
        if left_arr[i] <= right_arr[j]:
            # The value of arr at index k is set to left_arr at index i
            array[k] = left_arr[i]
            i += 1
        else:
            # Otherwise the value of arr at index k is set to right_arr at index j
            array[k] = right_arr[j]
            j += 1


query_list = [x for x in range(1000)]
random.shuffle(query_list)

st = time.process_time()

mergesort(query_list)

et = time.process_time()
res = et - st

print(query_list, f"\n {res} seconds")
