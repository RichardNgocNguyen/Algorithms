import random
import time


def mergesort(array, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if left < right:
        mid = (left + right) // 2
        mergesort(array, left, mid)
        mergesort(array, mid + 1, right)
        merge(array, left, mid, right)


def merge(array, left, mid, right):
    left_arr = []
    right_arr = []

    for i in range(left, mid + 1):
        left_arr.append(array[i])

    for j in range(mid + 1, right + 1):
        right_arr.append(array[j])

    left_arr.append(9999999999)
    right_arr.append(9999999999)

    i = j = 0
    for k in range(left, right + 1):
        if left_arr[i] <= right_arr[j]:
            array[k] = left_arr[i]
            i += 1
        else:
            array[k] = right_arr[j]
            j += 1


query_list = [x for x in range(1000)]
random.shuffle(query_list)

st = time.process_time()

mergesort(query_list)

et = time.process_time()
res = et - st

print(query_list, f"\n {res} seconds")
