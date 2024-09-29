import random
import sys
import time


def quicksort(array, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if left < right:
        q = partition(array, left, right)
        quicksort(array, left, q - 1)
        quicksort(array, q + 1, right)


def partition(array, left, right):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] > pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


sys.setrecursionlimit(1500)
query_list = [x for x in range(1000)]
random.shuffle(query_list)

st = time.process_time()

quicksort(query_list)

et = time.process_time()
res = et - st

print(query_list, f"\n {res} seconds")
