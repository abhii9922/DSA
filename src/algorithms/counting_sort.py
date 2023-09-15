def counting_sort(input_array):
  #find max and min value of the array
    max_val = max(input_array)
    min_val = min(input_array)

    #finding range
    count_array_length = max_val - min_val + 1

    # Initialize the count_array with  zeros
    count_array = [0] * count_array_length

    # Step 1 -> Traverse the input_array and increase
    # the corresponding count for every element by 1
    for el in input_array:
        count_array[el - min_val] += 1

    # Step 2 -> cummulative addition of count_array
    for i in range(1, count_array_length):
        count_array[i] += count_array[i-1]

    # Step 3 -> Calculate element position
    # based on the count_array values
    output_array = [0] * len(input_array)
    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i] - min_val] - 1] = input_array[i]
        count_array[input_array[i] - min_val] -= 1

    for i in range(len(input_array)):
        input_array[i] = output_array[i]
    return input_array


def sort(arr):
    sorted_arr = counting_sort(arr)
    return sorted_arr


