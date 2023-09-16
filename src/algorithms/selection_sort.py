def selection_sort(arr, size):
	#traverse through all the elements
	for idx in range(size):
		min_idx = idx
		#loop to find minimum element in rest of the array
		for j in range(idx + 1, size):
			# find minimum
			if arr[j] < arr[min_idx]:
				min_idx = j
		# swapping element with the first element
		(arr[idx], arr[min_idx]) = (arr[min_idx], arr[idx])

	return arr

def sort(arr):
	size = len(arr)
	sorted_arr = selection_sort(arr, size)
	return sorted_arr

