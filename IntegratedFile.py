from Algorithms import HeapSort,QuickSort,CountingSort,RadixSort,BucketSort
from matplotlib_module import plot_matplotlib
from random import randint
import time
#
ARRAY_LENGTH = 10000
arr = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
start = time.time()
sorted_heap = HeapSort.Sort(arr)
end = time.time()
exec_heap = end-start

arr = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
start = time.time()
sorted_quick = QuickSort.Sort(arr,0,len(arr)-1)
end = time.time()
exec_quick = end-start

arr = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
start = time.time()
sorted_count = CountingSort.countingSort(arr)
end = time.time()
exec_count = end-start

arr = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
start = time.time()
sorted_radix = RadixSort.radix_sort(arr)
end = time.time()
exec_radix = end-start

d = {"Input Values":[str(len(arr)),str(len(arr)),str(len(arr)),str(len(arr))],
   "Algorithm":["Heap_sort","Quick_sort","Counting_sort","Radix_sort"],
   "Space":[1,1,1,1],
   "Runtime":[exec_heap,exec_quick,exec_count,exec_radix]
   }

plot_obj=plot_matplotlib()
plot_obj.plot(d)
