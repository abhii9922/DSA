def countingSort(inputArray):
    # Find the maximum element in the inputArray
    maxElement= max(inputArray)

    countArrayLength = maxElement+1

    # Initialize the countArray with (max+1) zeros
    countArray = [0] * countArrayLength

    # Step 1 -> Traverse the inputArray and increase
    # the corresponding count for every element by 1
    for el in inputArray:
        countArray[el] += 1

    # Step 2 -> For each element in the countArray,
    # sum up its value with the value of the previous
    # element, and then store that value
    # as the value of the current element
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1]

    # Step 3 -> Calculate element position
    # based on the countArray values
    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray


def counting_sort2(arr):
    max_val = max(arr)
    min_val = min(arr)
    # print("min_val", min_val)
    # print("max_val", max_val)
    range_val = max_val - min_val + 1

    count = [0] * range_val
    output = [0] * len(arr)

    for num in arr:
        # print("num ", num, "num-min_val", num - min_val)
        count[num - min_val] += 1
        print(count)

    idx = 0
    for i in range(range_val):
        while count[i] > 0:
            output[idx] = i + min_val
            # print(output)
            idx += 1
            count[i] -= 1

    return output

#
# inputArray = [2,2,0,6,1,9,9,7]
# print("Input array = ", inputArray)
#
# sortedArray = counting_sort2(inputArray)
# print("Counting sort result = ", sortedArray)