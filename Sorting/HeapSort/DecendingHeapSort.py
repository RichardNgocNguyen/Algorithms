def left(x):
    return 2 * x + 1


def right(x):
    return 2 * x + 2


def build_heap(array):
    len_arr = len(array)
    for i in range(len_arr // 2):
        x = ((len_arr // 2) - 1) - i
        heapify(array, x)


def heapify(array, parent, heap_size=None):
    l = left(parent)
    r = right(parent)
    if heap_size is None:
        heap_size = len(arr)
    if l < heap_size and array[l] < array[parent]:
        smallest = l
    else:
        smallest = parent
    if r < heap_size and array[r] < array[smallest]:
        smallest = r
    if smallest != parent:
        array[parent], array[smallest] = array[smallest], array[parent]
        heapify(array, smallest, heap_size)


def heap_sort(array):
    build_heap(array)
    for i in range(len(array) - 1, 0, -1):
        heap_size = i
        array[0], array[heap_size] = array[heap_size], array[0]
        heapify(array, 0, heap_size)
    return array


arr = [1, 2, 3, 4, 5]
print(heap_sort(arr))
