import sys
sys.path.append('../')   
from DSA.Algorithms import HeapSort
from DSA.Algorithms import QuickSort
from DSA.Algorithms import MergeSort
from DSA.Algorithms import BubbleSort
from DSA.Algorithms import BucketSort
from DSA.Algorithms import CountingSort
from DSA.Algorithms import RadixSort

input_test_arrays = [[1, 12, 9, 5, 6, 10],
                    [-1, 12, 0, -5, 6, 10],
                    [29, 99, 27, -1, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]]

output_arrays = [ [1, 5, 6, 9, 10, 12],
                [-5, -1, 0, 6, 10, 12],
                [-1, 12, 19, 21, 27, 28, 29, 31, 44, 44, 58, 66, 76, 78, 83, 87, 88, 97, 99]]

def test_quicksort():
    input_test_arrays = [[1, 12, 9, 5, 6, 10],
                    [-1, 12, 0, -5, 6, 10],
                    [29, 99, 27, -1, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]]
    print("QUICK SORT:",end=" ")
    for i in range(len(input_test_arrays)):
        QuickSort.Sort(input_test_arrays[i], 0, len(input_test_arrays[i]) - 1)
        assert input_test_arrays[i] == output_arrays[i]
    print("PASSED")
      

def test_heapsort():
    input_test_arrays = [[1, 12, 9, 5, 6, 10],
                    [-1, 12, 0, -5, 6, 10],
                    [29, 99, 27, -1, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]]
    print("HEAP SORT:",end=" ")
    for i in range(len(input_test_arrays)):
        HeapSort.Sort(input_test_arrays[i])
        assert input_test_arrays[i] == output_arrays[i]
    print("PASSED")

def test_mergesort():
    input_test_arrays = [[1, 12, 9, 5, 6, 10],
                    [-1, 12, 0, -5, 6, 10],
                    [29, 99, 27, -1, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]]
    print("MERGE SORT:",end=" ")
    for i in range(len(input_test_arrays)):
        MergeSort.merge_sort(input_test_arrays[i])
        assert input_test_arrays[i] == output_arrays[i]
    print("PASSED")

def test_bubblesort():
    input_test_arrays = [[1, 12, 9, 5, 6, 10],
                    [-1, 12, 0, -5, 6, 10],
                    [29, 99, 27, -1, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]]
    print("BUBBLE SORT:",end=" ")
    for i in range(len(input_test_arrays)):
        BubbleSort.bubble_sort(input_test_arrays[i])
        assert input_test_arrays[i] == output_arrays[i]
    print("PASSED")

def test_radixsort():
    input_test_arrays = [[1, 12, 9, 5, 6, 10],
                    [-1, 12, 0, -5, 6, 10],
                    [29, 99, 27, -1, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]]
    print("RADIX SORT:",end=" ")
    for i in range(len(input_test_arrays)):
        print("Before",input_test_arrays[i])
        RadixSort.radix_sort(input_test_arrays[i])
        print("After",input_test_arrays[i])
        assert input_test_arrays[i] == output_arrays[i]

def test_countingsort():
    input_test_arrays = [[1, 12, 9, 5, 6, 10],
                    [-1, 12, 0, -5, 6, 10],
                    [29, 99, 27, -1, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]]
    print("COUNTING SORT:",end=" ")
    for i in range(len(input_test_arrays)):
        print("Before",input_test_arrays[i])
        CountingSort.countingSort(input_test_arrays[i])
        print("After",input_test_arrays[i])
        assert input_test_arrays[i] == output_arrays[i]

def test_bucketsort():
    input_test_arrays = [[1, 12, 9, 5, 6, 10],
                    [-1, 12, 0, -5, 6, 10],
                    [29, 99, 27, -1, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]]
    print("BUCKET SORT:",end=" ")
    for i in range(len(input_test_arrays)):
        print("Before",input_test_arrays[i])
        BucketSort.bucket_sort(input_test_arrays[i])
        print("After",input_test_arrays[i])
        assert input_test_arrays[i] == output_arrays[i]


test_quicksort()
test_heapsort()
test_mergesort()
test_bubblesort()
test_radixsort()
#test_countingsort()
#test_bucketsort()
