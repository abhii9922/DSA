from algorithms import *

#input_test_arrays
INPUT_TEST_CASES = {
    "Common use case": [1, 12, 9, 5, 6, 10],
    "Already sorted case": [2, 3, 11, 15, 23, 50, 51, 90, 91, 99],
    "Negative values present case": [-1, 12, 0, -5, 6, 10],
    "Bigger array with negative values case": [29, 99, 27, -1, 66, 28, 44, 0, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44],
}

EXCPECTED_OUTPUT = { 
    "Common use case": [1, 5, 6, 9, 10, 12],
    "Already sorted case": [2, 3, 11, 15, 23, 50, 51, 90, 91, 99],
    "Negative values present case": [-5, -1, 0, 6, 10, 12],
    "Bigger array with negative values case": [-1, 0, 12, 19, 21, 27, 28, 29, 31, 44, 44, 58, 66, 76, 78, 83, 87, 88, 97, 99]
}


# BUBBLE SORT
def test_bubblesort():
    print("BUBBLE SORT:")
    try:
        for key in INPUT_TEST_CASES:
            out = bubble_sort.sort(INPUT_TEST_CASES[key])
            assert out == EXCPECTED_OUTPUT[key]
            print("\t{}: OK".format(key))
    except:
        print("\t{}: FAILED".format(key))
        print("BUBBLE SORT FAILED")
    else:
        print("BUBBLE SORT PASSED")
    finally:
        print()


# BUCKET SORT
def test_bucketsort():
    print("BUCKET SORT:")
    try:
        for key in INPUT_TEST_CASES:
            out = bucket_sort.sort(INPUT_TEST_CASES[key])
            assert out == EXCPECTED_OUTPUT[key]
            print("\t{}: OK".format(key))
    except:
        print("\t{}: FAILED".format(key))
        print("BUCKET SORT FAILED")
    else:
        print("BUCKET SORT PASSED")
    finally:
        print()


# COUNTING SORT
def test_countingsort():    
    print("COUNTING SORT:")
    try:
        for key in INPUT_TEST_CASES:
            out = counting_sort.sort(INPUT_TEST_CASES[key])
            assert out == EXCPECTED_OUTPUT[key]
            print("\t{}: OK".format(key))
    except:
        print("\t{}: FAILED".format(key))
        print("COUNTING SORT FAILED")
    else:
        print("COUNTING SORT PASSED")
    finally:
        print()


# HEAP SORT
def test_heapsort():
    print("HEAP SORT:")
    try:
        for key in INPUT_TEST_CASES:
            out = heap_sort.sort(INPUT_TEST_CASES[key])
            assert out == EXCPECTED_OUTPUT[key]
            print("\t{}: OK".format(key))
    except:
        print("\t{}: FAILED".format(key))
        print("HEAP SORT FAILED")
    else:
        print("HEAP SORT PASSED")
    finally:
        print()
        


# INSERTION SORT
def test_insertionsort():
    print("INSERTION SORT:")
    try:
        for key in INPUT_TEST_CASES:
            out = insertion_sort.sort(INPUT_TEST_CASES[key])
            assert out == EXCPECTED_OUTPUT[key]
            print("\t{}: OK".format(key))
    except:
        print("\t{}: FAILED".format(key))
        print("INSERTION SORT FAILED")
    else:
        print("INSERTION SORT PASSED")
    finally:
        print()


# MERGE SORT
def test_mergesort():
    print("MERGE SORT:")
    try:
        for key in INPUT_TEST_CASES:
            out = merge_sort.sort(INPUT_TEST_CASES[key])
            assert out == EXCPECTED_OUTPUT[key]
            print("\t{}: OK".format(key))
    except:
        print("\t{}: FAILED".format(key))
        print("MERGE SORT FAILED")
    else:
        print("MERGE SORT PASSED")
    finally:
        print()


# QUICKSORT
def test_quicksort():
    print("QUICKSORT:")
    try:
        for key in INPUT_TEST_CASES:
            out = quicksort.sort(INPUT_TEST_CASES[key])
            assert out == EXCPECTED_OUTPUT[key]
            print("\t{}: OK".format(key))
    except:
        print("\t{}: FAILED".format(key))
        print("QUICKSORT SORT FAILED")
    else:
        print("QUICKSORT SORT PASSED")
    finally:
        print()


# RADIX SORT
def test_radixsort():
    radix_cases_expanded = {
        "Small values case": [1, 12, 9, 5, 6, 10],
        "Large values case": [8784, -9460, 4663, -8606, 1750, 2139, 9296, -9348, 8841, -2681, -4305, -5149, 4286, 4206, -1627, -4181, -5592, 4845, -5722, 753, -8688, 7714, 7465, -4323, -3014, -1025, -6415, 1872, -7898, -5754],
    }
    
    radix_expected_output_expanded = { 
        "Small values case": [1, 5, 6, 9, 10, 12],
        "Large values case": [-9460, -9348, -8688, -8606, -7898, -6415, -5754, -5722, -5592, -5149, -4323, -4305, -4181, -3014, -2681, -1627, -1025, 753, 1750, 1872, 2139, 4206, 4286, 4663, 4845, 7465, 7714, 8784, 8841, 9296],
    }

    radix_input_cases = INPUT_TEST_CASES | radix_expected_output_expanded
    radix_expected_output_cases = EXCPECTED_OUTPUT | radix_expected_output_expanded

    print("RADIX SORT:")
    try:
        for key in radix_input_cases:
            out = radix_sort.sort(radix_input_cases[key])
            assert out == radix_expected_output_cases[key]
            print("\t{}: OK".format(key))
    except:
        print("\t{}: FAILED".format(key))
        print("RADIX SORT FAILED")
    else:
        print("RADIX SORT PASSED")
    finally:
        print()


# SELECTION SORT
def test_selectionsort():
    print("SELECTION SORT:")
    try:
        for key in INPUT_TEST_CASES:
            out = selection_sort.sort(INPUT_TEST_CASES[key])
            assert out == EXCPECTED_OUTPUT[key]
            print("\t{}: OK".format(key))
    except:
        print("\t{}: FAILED".format(key))
        print("SELECTION SORT FAILED")
    else:
        print("SELECTION SORT PASSED")
    finally:
        print()


# main section -- start tests   
if __name__ == "__main__":
    test_bubblesort()
    test_bucketsort()
    test_countingsort()
    test_heapsort()
    test_insertionsort()
    test_mergesort()
    test_quicksort()
    test_radixsort()
    test_selectionsort()


