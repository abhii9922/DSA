# def insertionSort(b):
#     for i in range(1, len(b)):
#         up = b[i]
#         j = i - 1
#         while j >= 0 and b[j] > up:
#             b[j + 1] = b[j]
#             j -= 1
#         b[j + 1] = up
#     return b
#
#
# def BucketSort(input_list):
#     # maximum value in the list
#     # size of list
#     max_value = max(input_list)
#     size = max_value / len(input_list)
#
#     # Create n empty buckets where n = len of  input list
#     buckets_list = []
#     for x in range(len(input_list)):
#         buckets_list.append([])
#
#     # Put list elements into different buckets based on the size
#     for i in range(len(input_list)):
#         j = int(input_list[i] / size)
#         if j != len(input_list):
#             buckets_list[j].append(input_list[i])
#         else:
#             buckets_list[len(input_list) - 1].append(input_list[i])
#
#     # Sort elements within the buckets using Insertion Sort
#     for z in range(len(input_list)):
#         insertionSort(buckets_list[z])
#
#     # Concatenate buckets with sorted elements into a single list
#     final_output = []
#     for x in range(len(input_list)):
#         final_output = final_output + buckets_list[x]
#     return final_output
#

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        var = bucket[i]
        j = i - 1
        while j >= 0 and var < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = var
    return bucket


def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    min_val, max_val = min(arr), max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    for i in range(bucket_count):
        # Convert index to an integer
        idx = int((arr[i] - min_val) * (bucket_count - 1) / (max_val - min_val))
        buckets[idx].append(arr[i])

    for i in range(bucket_count):
        buckets[i] = insertion_sort(buckets[i])

    return [val for sublist in buckets for val in sublist]


# User input and demo
# arr = list(map(float, input("Enter space-separated numbers: ").split()))
# sorted_arr = bucket_sort(arr)
# print("Sorted Array:", sorted_arr)
