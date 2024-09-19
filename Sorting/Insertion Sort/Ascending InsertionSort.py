import time
import random


def insertion_sort(query):
    n = len(query)
    # get the start time
    st = time.process_time()
    # Starts from second element
    for i in range(1, n):
        # Saves a key
        key = query[i]
        # Set j as an index behind index i
        j = i - 1
        # Value of elements behind i is greater than element at j
        while j >= 0 and query[j] > key:
            # When while loop is true it will copy the element at index j to element at index j + 1
            query[j + 1] = query[j]
            j = j - 1
        # Sets j + 1 index in query top key
        query[j + 1] = key

    et = time.process_time()
    res = et - st
    return query, res


query_list = [x for x in range(1000)]
random.shuffle(query_list)
sorts = insertion_sort(query_list)
print(sorts[0], f"\n {sorts[1]}")
