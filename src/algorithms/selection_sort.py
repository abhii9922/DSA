def selection_sort(arr, size):
	for idx in range(size):
		min_idx = idx
		
		for j in range(idx + 1, size):
			# find minimum
			if arr[j] < arr[min_idx]:
				min_idx = j
		# swapping elements
		(arr[idx], arr[min_idx]) = (arr[min_idx], arr[idx])

	return arr

def sort(arr):
	size = len(arr)
	sorted_arr = selection_sort(arr, size)
	return sorted_arr

