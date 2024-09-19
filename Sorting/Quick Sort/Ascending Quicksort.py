import random
import sys
import time


def quicksort(array, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if left < right:
        # Calls the function to partition the array and return index of pivot
        q = partition(array, left, right)
        # Recursively calls the first half to be partitioned
        quicksort(array, left, q - 1)
        # Recursively calls the second half to be partitioned
        quicksort(array, q + 1, right)


def partition(array, left, right):
    # Sets the pivot
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        # if value at index j <= pivot, swap values in array at index i for index j
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    # Once the array is partitioned, swap value of array at index i + 1 for high
    array[i + 1], array[right] = array[right], array[i + 1]
    # Gives the index of the pivot
    return i + 1


sys.setrecursionlimit(1500)
query_list = [x for x in range(1000)]
random.shuffle(query_list)

st = time.process_time()

quicksort(query_list)

et = time.process_time()
res = et - st

print(query_list, f"\n {res} seconds")
