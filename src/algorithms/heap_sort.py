def heapify(input_array,len_heap,i):

    left_pointer = 2*i+1
    right_pointer = (2*i+2)
    largest = i
    if left_pointer < len_heap and input_array[left_pointer]>input_array[largest]:
        largest = left_pointer
    if right_pointer <len_heap and input_array[right_pointer]>input_array[largest]:
        largest = right_pointer

    #if root is not largest swap with the largest and continue maxheapify
    if largest != i:
        input_array[i],input_array[largest] = input_array[largest],input_array[i]
        heapify(input_array,len_heap,largest)


def sort(arr):
    heap_size = len(arr)

    # Build a maxheap.
    for i in range((heap_size // 2), -1, -1):
        heapify(arr, heap_size, i)

    #remove the root element and swap the last element as root and again heapify
    for i in range(heap_size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return arr






