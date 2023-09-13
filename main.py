from Plot.plot_module import seaborn_plot

#Test Dictionary
d={"Input Values":["1,2,3","4,5,6","7,8,9","10,11,12","13,14,15","1,2,3","4,5,6","7,8,9","10,11,12","13,14,15","1,2,3","4,5,6","7,8,9","10,11,12","13,14,15",
                   "1,2,3","4,5,6","7,8,9","10,11,12","13,14,15","1,2,3","4,5,6","7,8,9","10,11,12","13,14,15"],
   "Algorithm":["Bubble Sort","Bubble Sort","Bubble Sort","Bubble Sort","Bubble Sort",
                "Merge Sort","Merge Sort","Merge Sort","Merge Sort","Merge Sort",
                "Bucket Sort","Bucket Sort","Bucket Sort","Bucket Sort","Bucket Sort",
                "Insertion Sort","Insertion Sort","Insertion Sort","Insertion Sort","Insertion Sort",
                "Counting Sort","Counting Sort","Counting Sort","Counting Sort","Counting Sort"],
   "Space":[1,2,3,4,5,3,4,2,1,6,4,2,1,5,3,2,3,5,2,4,2,6,3,1,4],
   "Runtime":[4.65,3.84,3.95,3.05,5.04,3.23,4.45,1.83,3.65,2.34,5.78,4.76,3.23,4.43,3.43,2.54,3.23,4.43,3.43,2.54,3.23,4.10,3.85,3.33,2.95]
   }
"""
   Input Values       Algorithm  Space  Runtime
0         1,2,3     Bubble Sort      1     4.65
1         4,5,6     Bubble Sort      2     3.84
2         7,8,9     Bubble Sort      3     3.95
3      10,11,12     Bubble Sort      4     3.05
4      13,14,15     Bubble Sort      5     5.04
5         1,2,3      Merge Sort      3     3.23
6         4,5,6      Merge Sort      4     4.45
7         7,8,9      Merge Sort      2     1.83
8      10,11,12      Merge Sort      1     3.65
9      13,14,15      Merge Sort      6     2.34
10        1,2,3     Bucket Sort      4     5.78
11        4,5,6     Bucket Sort      2     4.76
12        7,8,9     Bucket Sort      1     3.23
13     10,11,12     Bucket Sort      5     4.43
14     13,14,15     Bucket Sort      3     3.43
15        1,2,3  Insertion Sort      2     2.54
16        4,5,6  Insertion Sort      3     3.23
17        7,8,9  Insertion Sort      5     4.43
18     10,11,12  Insertion Sort      2     3.43
19     13,14,15  Insertion Sort      4     2.54
20        1,2,3   Counting Sort      2     3.23
21        4,5,6   Counting Sort      6     4.10
22        7,8,9   Counting Sort      3     3.85
23     10,11,12   Counting Sort      1     3.33
24     13,14,15   Counting Sort      4     2.95
"""
#Create an object 
plot_obj=seaborn_plot()

#Call its method and pass the data to it
plot_obj.plot(d)

#Delete the object
del plot_obj
