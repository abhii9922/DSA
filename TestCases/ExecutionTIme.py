import time
from random import randint
from timeit import repeat
from Algorithms import HeapSort
from Algorithms import QuickSort



ARRAY_LENGTH = 10000

if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    n_arrays = []
    for i in range(3):
        n_arrays.append([randint(0, 1000) for i in range(ARRAY_LENGTH)])

    # Call the function using the name of the sorting algorithm
    # and the array you just created
    eff = []
    for i in range(3):
        start = time.time()
        # print(n_arrays[i])i
        QuickSort.Sort(n_arrays[i],start = 0,end = len(n_arrays[i])-1)
        end = time.time()
        efficiency = end - start
        eff.append(efficiency)
    print(min(eff))
