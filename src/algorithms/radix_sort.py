def radix_sort(array):

    max_num = max(array)
    exp = 1
    n = len(array)
    output = [0] * n

    while max_num // exp > 0:

        counting = [0] * 10

        for i in array:
            counting[(i // exp) % 10] += 1

        for i in range(1, 10):
            counting[i] += counting[i - 1]
            
        for i in range(n - 1, -1, -1):
            output[counting[(array[i] // exp) % 10] - 1] = array[i]
            counting[(array[i] // exp) % 10] -= 1

        for i in range(n):
            array[i] = output[i]

        exp *= 10

    return array


def sort(arr):
    sorted_arr = radix_sort(arr)
    return sorted_arr