import time


def binarySearch(query, target, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(query) - 1

    mid = (left + right) // 2

    if right >= left:
        if query[mid] == target:
            return mid
        elif query[mid] < target:
            return binarySearch(query, target, mid + 1, right)
        elif query[mid] > target:
            return binarySearch(query, target, left, mid - 1)
    else:
        return None


query_list = [x for x in range(500)]

st = time.process_time()

index = binarySearch(query_list, target=273)

et = time.process_time()
res = et - st

print("Found Target:", index, f"\n {res} seconds")


