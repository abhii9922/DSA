
RADIX = 10
def radix_sort_nonneg(lst):
    last_iteration = False
    radix_power = 1
    while not last_iteration:
        # split into buckets
        buckets = [[] for _ in range(RADIX)]
        last_iteration = True  # unless we find it isn't
        for el in lst:
            # find the digit corresponding to radix_power
            digit = el % (radix_power*RADIX) // radix_power
            buckets[digit].append(el)
            if el >= radix_power*RADIX:
                last_iteration = False

        # flatten
        lst = [el for bucket in buckets for el in bucket]
        radix_power *= RADIX
    return lst


def radix_sort(lst):
    positive_ints = radix_sort_nonneg( x for x in lst if x >= 0)
    negative_ints = radix_sort_nonneg(-x for x in lst if x <  0)
    return [-x for x in reversed(negative_ints)] + positive_ints


def sort(arr):
    sorted_arr = radix_sort(arr)
    return sorted_arr

# print(sort([1, 12, 9, 5, 6, 10]))

