from Algorithms import HeapSort
from Algorithms import QuickSort


def test_quicksort():
    input_arrays = [[1, 12, 9, 5, 6, 10],
                    [-1, 12, 0, -5, 6, 10],
                    [29, 99, 27, -1, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]]
    for i in range(len(input_arrays)):
        print("before",input_arrays[i])
        QuickSort.quick_sort(input_arrays[i], 0, len(input_arrays[i]) - 1)
        print("after",input_arrays[i])

def test_heapsort():
    input_arrays = [[1, 12, 9, 5, 6, 10],
                    [-1, 12, 0, -5, 6, 10],
                    [29, 99, 27, -1, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]]
    for i in input_arrays:
        print("before",i)
        HeapSort.heapSort(i)
        print("after",i)


test_quicksort()
test_heapsort()
