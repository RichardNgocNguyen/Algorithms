def left(x):
    return 2 * x + 1


def right(x):
    return 2 * x + 2


def heapify(array, parent, heap_size=None):
    l = left(parent)
    r = right(parent)
    # Only needed for sorting the heap
    if heap_size is None:
        heap_size = len(array)
    # comparison of heap_size for sorting
    # Checks if the left child of parent is larger and sets largest to that child
    if l < heap_size and array[l] > array[parent]:
        largest = l
    # Else parent is still larger and sets that as largest
    else:
        largest = parent
    # comparison of heap_size for sorting
    # Checks if the right child larger by checking what set as largest(parent or left child), and set as largest
    if r < heap_size and array[r] > array[largest]:
        largest = r
    # If the largest is not the parent, swap for the largest(left child or right child)
    if largest != parent:
        array[parent], array[largest] = array[largest], array[parent]
        # heapify to see if the largest child should be pushed up the heap
        heapify(array, largest, heap_size)


def build_heap(array):
    len_arr = len(array)
    # For loop with backward pointer that travels from the end to mid of list, and heapifies
    for i in range(len_arr // 2):
        x = ((len_arr // 2) - 1) - i
        heapify(array, x)


def heap_sort(array):
    # Build a heap
    build_heap(array)
    # Reverse for loop
    for i in range(len(array) - 1, 0, -1):
        heap_size = i
        # Move the largest element to the back at index heap_size
        array[0], array[heap_size] = array[heap_size], array[0]
        # Heapifies the array and stops before heap_size index is reached
        heapify(array, 0, heap_size)

    return array


arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(heap_sort(arr))
