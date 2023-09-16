def bubble_sort(arr):
    n = len(arr)
    # traverse through all the elements
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            #swap if element found is greater
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        #if not swapped (boolean) then break the loop
        if not swapped:
            break
    return arr


def sort(arr):
    sorted_arr = bubble_sort(arr)
    return sorted_arr


