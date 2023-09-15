# analysis Module
#	- contains methods for running runtime and space complexity analyses
#	- returns data that can be used for visualization

import sys
import time
import tracemalloc

# measure RUNTIME of MULTIPLE algorithms on a SINGLE set of data
def sorting_runtime_all(input_data, algorithms):
	results = {}
	for algorithm_name, algorithm_function in algorithms.items():
		sorted_data, time_taken = sorting_runtime_one(algorithm_function, input_data)
		results[algorithm_name] = (sorted_data, time_taken)

	# sample results value:  
	# { 'Bubble Sort': ([2, 33, 42], 3.3855438232421875e-05), 
	# 	'Bucket Sort': ([2, 33, 42], 4.00543212890625e-05), 
	#	...
	#	'Quicksort': ([2, 33, 42], 1.621246337890625e-05), 
	#	'Radix Sort': ([2, 33, 42], 3.0040740966796875e-05)	}
	return results


# measure RUNTIME of a SINGLE algorithm on a SINGLE set of data
def sorting_runtime_one(algorithm_function, input_data):
	unsorted_data = input_data.copy()	# Make a copy to avoid modifying the original data
	"""
	if sys.platform == "win32":
	    # on Windows, the best timer is time.clock()
	    default_timer = time.clock
	else:
	    # on most other platforms the best timer is time.time()
	    default_timer = time.time
	"""

        #No use of default_timer
	#default_timer=time.process_time

	start_time = time.process_time()
	sorted_data = algorithm_function(unsorted_data)  
	end_time = time.process_time()

	time_taken = end_time - start_time

	return sorted_data, time_taken


# measure MEMORY usage of MULTIPLE algorithms on a SINGLE set of data
def sorting_memory_all(input_data, algorithms):
	results = {}
	for algorithm_name, algorithm_function in algorithms.items():
		sorted_data, max_memory_allocated = sorting_memory_one(algorithm_function, input_data)
		results[algorithm_name] = (sorted_data, max_memory_allocated)

	return results


# measure MEMORY usage of a SINGLE algorithm on a SINGLE set of data
def sorting_memory_one(algorithm_function, input_data):
	unsorted_data = input_data.copy()	# Make a copy to avoid modifying the original data
	
	tracemalloc.start()
	sorted_data = algorithm_function(unsorted_data)  
	current, peak_size = tracemalloc.get_traced_memory()
	tracemalloc.stop()

	return sorted_data, peak_size
