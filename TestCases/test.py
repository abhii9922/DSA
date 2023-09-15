import sys
sys.path.append('../')   
from DSA.src.algorithms import heap_sort
from DSA.src.algorithms import quicksort
from DSA.src.algorithms import merge_sort
from DSA.src.algorithms import bubble_sort
from DSA.src.algorithms import bucket_sort
from DSA.src.algorithms import counting_sort
from DSA.src.algorithms import radix_sort

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
        quicksort.sort(input_test_arrays[i])
        assert input_test_arrays[i] == output_arrays[i]
    print("PASSED")
      

def test_heapsort():
    input_test_arrays = [[1, 12, 9, 5, 6, 10],
                    [-1, 12, 0, -5, 6, 10],
                    [29, 99, 27, -1, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]]
    print("HEAP SORT:",end=" ")
    for i in range(len(input_test_arrays)):
        heap_sort.sort(input_test_arrays[i])
        assert input_test_arrays[i] == output_arrays[i]
    print("PASSED")

def test_mergesort():
    input_test_arrays = [[1, 12, 9, 5, 6, 10],
                    [-1, 12, 0, -5, 6, 10],
                    [29, 99, 27, -1, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]]
    print("MERGE SORT:",end=" ")
    for i in range(len(input_test_arrays)):
        merge_sort.sort(input_test_arrays[i])
        assert input_test_arrays[i] == output_arrays[i]
    print("PASSED")

def test_bubblesort():
    input_test_arrays = [[1, 12, 9, 5, 6, 10],
                    [-1, 12, 0, -5, 6, 10],
                    [29, 99, 27, -1, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]]
    print("BUBBLE SORT:",end=" ")
    for i in range(len(input_test_arrays)):
        bubble_sort.sort(input_test_arrays[i])
        assert input_test_arrays[i] == output_arrays[i]
    print("PASSED")

def test_radixsort():
    input_test_arrays = [[1, 12, 9, 5, 6, 10],
                    [1, 121, 34, 46, 6, 10]]
    
    output_arrays = [ [1, 5, 6, 9, 10, 12],
                [1, 6, 10, 34, 46, 121]]
    
    print("RADIX SORT:",end=" ")
    for i in range(len(input_test_arrays)):
        radix_sort.sort(input_test_arrays[i])
        assert input_test_arrays[i] == output_arrays[i]
    print("PASSED")

def test_countingsort():
    input_test_arrays = [[1, 12, 9, 5, 6, 10],
                    [1, 121, 34, 46, 6, 10]]
    
    output_arrays = [ [1, 5, 6, 9, 10, 12],
                [1, 6, 10, 34, 46, 121]]
    
    print("COUNTING SORT:",end=" ")
    for i in range(len(input_test_arrays)):
        print("Before",input_test_arrays[i])
        counting_sort.sort(input_test_arrays[i])
        print("After",input_test_arrays[i])
        assert input_test_arrays[i] == output_arrays[i]
    print("PASSED")

def test_bucketsort():
    input_test_arrays = [[1, 12, 9, 5, 6, 10, 11 ,12 ,13,14,15],
                    [1, 121, 34, 46, 6, 10]]
    
    output_arrays = [ [1, 5, 6, 9, 10, 11, 12, 13, 14, 15],
                [1, 6, 10, 34, 46, 121]]
    
    print("BUCKET SORT:",end=" ")
    for i in range(len(input_test_arrays)):
        print("Before",input_test_arrays[i])
        bucket_sort.sort(input_test_arrays[i])
        print("After",input_test_arrays[i])
        assert input_test_arrays[i] == output_arrays[i]
    print("PASSED")


test_quicksort()
test_heapsort()
test_mergesort()
test_bubblesort()
test_radixsort()
#test_countingsort()
test_bucketsort()
