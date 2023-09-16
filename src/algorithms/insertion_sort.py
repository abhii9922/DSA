def insertion_sort(arr):
    #traversing from first element  to end of the array
    for i in range(1, len(arr)):
        var = arr[i]
        j = i - 1

        # reverse sorting till array[j]
        while j >= 0 and var < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = var
    return arr

def sort(arr):
    sorted_arr = insertion_sort(arr)
    return sorted_arr


