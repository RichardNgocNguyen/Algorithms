import time
import random


def insertion_sort(query):
    st = time.process_time()

    n = len(query)
    for i in range(1, n):
        key = query[i]
        j = i - 1
        while j >= 0 and query[j] > key:
            query[j + 1] = query[j]
            j = j - 1
        query[j + 1] = key

    et = time.process_time()
    res = et - st
    return query, res


query_list = [x for x in range(1000)]
random.shuffle(query_list)
sorts = insertion_sort(query_list)
print(sorts[0], f"\n {sorts[1]}")
