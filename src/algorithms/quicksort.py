def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high


def quicksort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quicksort(array, start, p-1)
    quicksort(array, p+1, end)
    return array


def sort(array):
    start = 0
    end = len(array) - 1
    sorted_arr = quicksort(array, start, end)
    return sorted_arr





