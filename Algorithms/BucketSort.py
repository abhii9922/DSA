def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def BucketSort(input_list):
    # maximum value in the list
    # size of list
    max_value = max(input_list)
    size = max_value / len(input_list)

    # Create n empty buckets where n = len of  input list
    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([])

    # Put list elements into different buckets based on the size
    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    # Sort elements within the buckets using Insertion Sort
    for z in range(len(input_list)):
        insertionSort(buckets_list[z])

    # Concatenate buckets with sorted elements into a single list
    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]
    return final_output
