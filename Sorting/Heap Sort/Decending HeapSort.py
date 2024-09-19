def left(x):
    return 2 * x + 1


def right(x):
    return 2 * x + 2


def build_heap(array):
    len_arr = len(array)
    # For loop with backward pointer that travels from the end to mid of list, and heapifies
    for i in range(len_arr // 2):
        x = ((len_arr // 2) - 1) - i
        descend_heapify(array, x)


def descend_heapify(array, parent, heap_size=None):
    l = left(parent)
    r = right(parent)
    # Only needed for sorting the heap
    if heap_size is None:
        heap_size = len(arr)
    # comparison of heap_size for sorting
    # Checks if the left child of parent is smaller and sets smallest to that child
    if l < heap_size and array[l] < array[parent]:
        smallest = l
    # Else parent is still smaller and sets that as smallest
    else:
        smallest = parent
    # comparison of heap_size for sorting
    # Checks if the right child smaller by checking what set as smallest(parent or left child), and set as smallest
    if r < heap_size and array[r] < array[smallest]:
        smallest = r
    # If the smallest is not the parent, swap for the smallest(left child or right child)
    if smallest != parent:
        array[parent], array[smallest] = array[smallest], array[parent]
        # heapify to see if the smallest child should be pushed up the heap
        descend_heapify(array, smallest, heap_size)


def heap_sort(array):
    # Build a heap
    build_heap(array)
    # Reverse for loop
    for i in range(len(array) - 1, 0, -1):
        heap_size = i
        # Move the smallest element to the back at index heap_size
        array[0], array[heap_size] = array[heap_size], array[0]
        # Heapifies the array and stops before heap_size index is reached
        descend_heapify(array, 0, heap_size)

    return array


arr = [1, 2, 3, 4, 5]
print(heap_sort(arr))
