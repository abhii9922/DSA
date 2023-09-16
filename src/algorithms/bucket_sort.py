# def insertion_sort(bucket):
#     for i in range(1, len(bucket)):
#         var = bucket[i]
#         j = i - 1
#         while j >= 0 and var < bucket[j]:
#             bucket[j + 1] = bucket[j]
#             j -= 1
#         bucket[j + 1] = var
#     return bucket

from algorithms.insertion_sort import insertion_sort



def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    min_val, max_val = min(arr), max(arr)  # for minimum and maximum value of the array
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    #put array elements into buckets
    for i in range(bucket_count):
        # Convert index to an integer
        idx = int((arr[i] - min_val) * (bucket_count - 1) / (max_val - min_val))
        buckets[idx].append(arr[i])

    # sorting elements in individual buckets
    for i in range(bucket_count):
        buckets[i] = insertion_sort(buckets[i])

    return [val for sublist in buckets for val in sublist]


def sort(arr):
    sorted_arr = bucket_sort(arr)
    return sorted_arr

