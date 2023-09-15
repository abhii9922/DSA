def insertion_sort(arr):
    for i in range(1, len(arr)):
        var = arr[i]
        j = i - 1
        while j >= 0 and var < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = var
    return arr

def sort(arr):
    sorted_arr = insertion_sort(arr)
    return sorted_arr